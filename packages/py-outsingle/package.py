# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyOutsingle(PythonPackage):
    """OutSingle - A Python tool for finding outliers in RNA-Seq gene expression count data using SVD/OHT."""

    homepage = "https://github.com/esalkovic/outsingle"
    url = "https://github.com/esalkovic/outsingle/archive/refs/heads/master.zip"
    git = "https://github.com/esalkovic/outsingle.git"

    version("20230324", commit="d7da6d74f8d8412480cb3fa02d3d26ba240f7c0b")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-mpmath", type=("build", "run"))
    depends_on("py-multiprocess", type=("build", "run"))

    def patch(self):
        # Create pyproject.toml for installation
        with open("pyproject.toml", "w") as fh:
            fh.write(
                """[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "outsingle"
version = "0.1.0"
description = "A tool for finding outliers in RNA-Seq gene expression count data using SVD/OHT"
readme = "README.rst"
authors = [{name = "Edin Salkovic"}]
license = {text = "BSD-3-Clause"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
]
dependencies = [
    "numpy",
    "scipy",
    "pandas",
    "mpmath",
    "multiprocess",
]
"""
            )

        # Create setup.py file with proper package discovery
        with open("setup.py", "w") as fh:
            fh.write(
                """from setuptools import setup, find_packages

setup(
    name="outsingle",
    packages=find_packages(),
    package_data={
        "outsingle": ["*.py"],
    },
)
"""
            )

        # Create package structure
        os.makedirs("outsingle", exist_ok=True)

        # Create __init__.py
        with open("outsingle/__init__.py", "w") as fh:
            fh.write("# OutSingle package\n")

        # Copy helper modules to the package
        import shutil

        if os.path.exists("helpers.py"):
            shutil.copy("helpers.py", "outsingle/")
        if os.path.exists("optht.py"):
            shutil.copy("optht.py", "outsingle/")

        # Process scripts and add them to the package
        script_files = ["fast_zscore_estimation.py", "optht_svd_zs.py", "inject_outliers_fzse_pysvdcc.py"]

        for script in script_files:
            # Read the original script
            with open(script, "r") as f:
                content = f.read()

            # Update imports to use the package namespace
            content = content.replace("import helpers", "from outsingle import helpers")
            content = content.replace("import optht", "from outsingle import optht")
            content = content.replace("from helpers", "from outsingle.helpers")
            content = content.replace("from optht", "from outsingle.optht")

            # Write the updated script to the package
            with open(f"outsingle/{script}", "w") as f:
                f.write(content)

    @run_after("install")
    def post_install(self):
        # Create bin directory with executable scripts
        mkdirp(self.prefix.bin)

        # Copy scripts to bin with proper permissions
        script_files = ["fast_zscore_estimation.py", "optht_svd_zs.py", "inject_outliers_fzse_pysvdcc.py"]

        for script in script_files:
            # Create executable script that uses the installed module
            with open(join_path(self.prefix.bin, script), "w") as f:
                f.write(f"""#!/usr/bin/env python
from outsingle.{script.replace('.py', '')} import main

if __name__ == "__main__":
    main()
""")
            # Make executable
            os.chmod(join_path(self.prefix.bin, script), 0o755)
