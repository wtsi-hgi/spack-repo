# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGnomix(PythonPackage):
    """High Resolution Ancestry Deconvolution for Next Generation Genomic Data."""

    homepage = "https://github.com/AI-sandbox/gnomix"
    pypi = "gnomix/gnomix-0.0.7.tar.gz"

    version("0.0.7", sha256="11ff33182481cf74fd875e4be4ffc5b0709fd5803b434a92cfe3c20463e28bb3")

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
