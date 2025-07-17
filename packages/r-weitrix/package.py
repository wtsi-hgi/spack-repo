# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeitrix(RPackage):
    """Tools for matrices with precision weights, test and explore weighted or sparse data

    Data type and tools for working with matrices having precision weights and missing data. This package provides a common representation and tools that can be used with many types of high-throughput data. The meaning of the weights is compatible with usage in the base R function "lm" and the package "limma". Calibrate weights to account for known predictors of precision. Find rows with excess variability. Perform differential testing and find rows with the largest confident differences. Find PCA-like components of variation even with many missing values, rotated so that individual components may be meaningfully interpreted. DelayedArray matrices and BiocParallel are supported.
    """

    bioc = "weitrix"

    version("1.20.0", commit="1269ffd7c60aa296ab27e28f8f821b2e3096e8c6")
    version("1.14.0", commit="263312072f9ae115cf7c24c4b946b733ee5f5306")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-topconfects", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ckmeans-1d-dp", type=("build", "run"))
    depends_on("r-glm2", type=("build", "run"))
    depends_on("r-rhpcblasctl", type=("build", "run"))
