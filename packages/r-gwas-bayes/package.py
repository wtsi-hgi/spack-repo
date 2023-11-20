# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGwasBayes(RPackage):
    """This package is built to perform GWAS analysis using Bayesian techniques. Currently, GWAS.BAYES has functionality for the implementation of BICOSS for Gaussian phenotypes."""

    url = "https://bioconductor.org/packages/release/bioc/src/contrib/GWAS.BAYES_1.12.0.tar.gz"
    bioc = "GWAS.BAYES"

    version("1.12.0", sha256="4b7b8bd9f541a6dba8ac812683bc160def6b8605d1fca7a86ff5887b2cb97fec")

    depends_on("r-ga@3.2:", type=("build", "run"))
    depends_on("r-caret@6.0-86:", type=("build", "run"))
    depends_on("r-memoise@1.1.0:", type=("build", "run"))
    depends_on("r-matrix@1.2-18:", type=("build", "run"))
    depends_on("r-limma@3.54.0:", type=("build", "run"))
    depends_on("r-mass@7.3-58.1:", type=("build", "run"))
