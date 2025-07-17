# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsnid(RPackage):
    """Utilities for Exploration and Assessment of Confidence of LC-MSn Proteomics Identifications

    Extracts MS/MS ID data from mzIdentML (leveraging mzID package) or text files. After collating the search results from multiple datasets it assesses their identification quality and optimize filtering criteria to achieve the maximum number of identifications while not exceeding a specified false discovery rate. Also contains a number of utilities to explore the MS/MS results and assess missed and irregular enzymatic cleavages, mass measurement accuracy, etc.
    """

    bioc = "MSnID"

    version("1.42.0", commit="6adbfffa8076e7e7380d7ff1472d0c58423d6485")
    version("1.36.0", commit="605438ebf11bfc0edc9ca2fc64ae5549e14a2eea")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-msnbase@1.12.1:", type=("build", "run"))
    depends_on("r-mzid@1.3.5:", type=("build", "run"))
    depends_on("r-r-cache", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-iterators", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-protgenerics", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-mzr", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-msmstests", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-runit", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))
