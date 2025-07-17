# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPharmacogx(RPackage):
    """Analysis of Large-Scale Pharmacogenomic Data

    Contains a set of functions to perform large-scale analysis of pharmaco-genomic data. These include the PharmacoSet object for storing the results of pharmacogenomic experiments, as well as a number of functions for computing common summaries of drug-dose response and correlating them with the molecular features in a cancer cell-line.
    """

    bioc = "PharmacoGx"

    version("3.12.2", commit="6309546a2410eaa09aee8ed0d73d226d6dd52501")
    version("3.6.0", commit="449b0a6cfcbbfbe27c8cec1f55fbaa4c6f011228")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-coregx", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magicaxis", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-catools", type=("build", "run"))
    depends_on("r-downloader", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-coop", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
