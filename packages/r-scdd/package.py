# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdd(RPackage):
    """Mixture modeling of single-cell RNA-seq data to identify genes with differential distributions

    This package implements a method to analyze single-cell RNA- seq Data utilizing flexible Dirichlet Process mixture models. Genes with differential distributions of expression are classified into several interesting patterns of differences between two conditions. The package also includes functions for simulating data with these patterns from negative binomial distributions.
    """

    homepage = "https://github.com/kdkorthauer/scDD"
    bioc = "scDD"

    version("1.32.0", commit="1e76275e4928ed494d88c5cc2ad58d6d7725e5c5")
    version("1.26.0", commit="6a08730f5e23c5620187627c479821f9b4e431c9")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-fields", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-outliers", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ebseq", type=("build", "run"))
    depends_on("r-arm", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
