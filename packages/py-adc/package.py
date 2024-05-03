# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAdc(PythonPackage):
    """ADC is an efficient method to identify highly interrelated genes across datasets. The source code and a demo file are provided. We provide an easy-to-use api to realize ADC and our code is well annotated."""

    homepage = "https://github.com/zhanglabtools/ADC"
    git = "https://github.com/zhanglabtools/ADC.git"

    version("2021-09-16", commit="308f395f850f694b25c9505ab7ed91bdb6de0deb")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-tqdm+notebook", type=("build", "run"))

    def patch(self):
        filter_file("from dcorT import *", "from .dcorT import *", "ADC.py", string=True)
        filter_file("from BCDCOR import *", "from .BCDCOR import *", "dcorT.py", string=True)
        mkdir("ADC")
        for file in ["data", "ADC.py", "BCDCOR.py", "dcorT.py", "__init__.py"]:
            move(file, "ADC")

        with open("setup.py", "w") as fh:
            fh.write("from setuptools import setup\nsetup()")

        with open("pyproject.toml", "w") as fh:
            fh.write("[project]\nname = \"ADC\"\nversion = \"2021.09.16\"\ndependencies = [\"numpy\", \"sklearn\", \"scipy\", \"pandas\", \"tqdm\"]\n[tool.setuptools.packages.find]\nwhere = [\".\"]")
