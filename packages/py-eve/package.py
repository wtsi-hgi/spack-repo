# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyEve(PythonPackage):
    """EVE (Evolutionary model of Variant Effects) provides protein-specific models
    for predicting pathogenicity of amino acid mutations using deep generative
    models trained on evolutionary data."""

    homepage = "https://evemodel.org"
    url = "https://github.com/OATML-Markslab/EVE/archive/refs/heads/master.tar.gz"
    git = "https://github.com/OATML-Markslab/EVE.git"

    version("20220111", commit="460d70efeeeded58bc69227a203540d68953ae88")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-torch-gpu", type=("build", "run"))
    depends_on("py-scikit-learn@0.24.1:", type=("build", "run"))
    depends_on("py-numpy@1.20.1:", type=("build", "run"))
    depends_on("py-pandas@1.2.4:", type=("build", "run"))
    depends_on("py-scipy@1.6.2:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))

    def patch(self):
        # Create pyproject.toml to properly package the module
        with open("pyproject.toml", "w") as f:
            f.write("""
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "eve"
version = "1.0.0"
authors = [
    {name = "Jonathan Frazer et al.", email = "example@example.com"}
]
description = "Evolutionary model of Variant Effects (EVE)"
readme = "README.md"
requires-python = ">=3.7"
dependencies = [
    "torch>=1.7",
    "scikit-learn>=0.24.1",
    "numpy>=1.20.1",
    "pandas>=1.2.4", 
    "scipy>=1.6.2",
    "tqdm",
    "matplotlib",
    "seaborn"
]
""")

        # Create setup.py for package structure
        with open("setup.py", "w") as f:
            f.write("""
from setuptools import setup, find_packages

setup(
    name="eve",
    packages=find_packages(include=["EVE", "EVE.*", "utils", "utils.*"]),
    package_data={
        "EVE": ["data/MSA/*", "data/labels/*"],
    },
)
""")

        # Create __init__.py files
        touch("EVE/__init__.py")
        touch("utils/__init__.py")

    @run_after("install")
    def install_scripts(self):
        mkdirp(self.prefix.bin)
        for script in ["train_VAE.py", "compute_evol_indices.py", "train_GMM_and_compute_EVE_scores.py"]:
            with open(script, "r") as f:
                content = f.read()
            with open(join_path(self.prefix.bin, script), "w") as f:
                f.write("#!/usr/bin/env python\n" + content)
            os.chmod(join_path(self.prefix.bin, script), 0o755)
