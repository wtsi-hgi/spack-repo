# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class Pridict2(PythonPackage):
    """PRIDICT2.0 is an advanced version of the original PRIDICT model designed for predicting the efficiency of prime editing guide RNAs. This repository allows you to run the model locally."""

    homepage = "https://www.biorxiv.org/content/10.1101/2023.10.09.561414v1"
    git = "https://github.com/uzh-dqbm-cmi/PRIDICT2"

    version("2024-03-05", commit="20baae33ffda52019b440498f71d86626114c4cc")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-torchaudio", type=("build", "run"))
    depends_on("py-tensorflow", type=("build", "run"))
    depends_on("py-biopython", type="run")
    depends_on("py-pandas", type="run")
    depends_on("py-tqdm", type="run")
    depends_on("py-scipy", type="run")
    depends_on("py-scikit-learn", type="run")
    depends_on("py-prettytable", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-keras", type="run")
    depends_on("py-joblib", type="run")
    depends_on("py-primer3-py", type="run")

    patch("shbang.patch")

    def patch(self):
        filter_file("#!/usr/bin/python", "#!"+self.spec["python"].prefix.bin.python, "pridict2_pegRNA_design.py", string=True)

        with open("pyproject.toml", "w") as fh:
            fh.write("[project]\nname = \"Predict2\"\nversion = \"2024.03.05\"\ndependencies = [\"torch\", \"torchvision\", \"torchaudio\", \"tensorflow\"]\n[tool.setuptools.packages.find]\nwhere = [\".\"]")
        
    @run_after("install")
    def post(self):
        mkdir(self.prefix.bin)
        os.chmod("pridict2_pegRNA_design.py", 0o755)
        install("pridict2_pegRNA_design.py", self.prefix.bin)
