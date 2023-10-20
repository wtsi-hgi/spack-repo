# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *

class PyGnomix(PythonPackage):
    """High Resolution Ancestry Deconvolution for Next Generation Genomic Data."""

    homepage = "https://github.com/AI-sandbox/gnomix"
    git = "https://github.com/AI-sandbox/gnomix"

    version("0.0.7", commit="de952a296c4e9bcf7a5b204667147122e33c1a03")

    depends_on("python@3.7.4:", type=("build", "run"))
    depends_on("py-matplotlib@3.3.4:")
    depends_on("py-numpy@1.20.3:")
    depends_on("py-pandas@1.3.5:")
    depends_on("py-pyyaml@5.1.2:")
    depends_on("py-scikit-allel@1.3.1:")
    depends_on("py-scikit-learn@1.0.1:")
    depends_on("py-scipy@1.5.3:")
    depends_on("py-seaborn@0.11.2:")
    depends_on("py-sklearn-crfsuite@0.3.6:")
    depends_on("py-tqdm@4.62.3:")
    depends_on("py-uncertainty-calibration@0.0.7:")
    depends_on("py-xgboost@1.1.1:")

    def install(self, spec, prefix):
        with open('./gnomix.py', 'r') as fh:
            data = fh.read()

        with open('./gnomix.py', 'w') as fh:
            fh.write("#!/usr/bin/env python3\n" + data)

        os.chmod("./gnomix.py", 0o755)
        install_tree(".", prefix)
