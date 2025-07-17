# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathvar(RPackage):
    """Methods to Find Pathways with Significantly Different Variability

    This package contains the functions to find the pathways that have significantly different variability than a reference gene set. It also finds the categories from this pathway that are significant where each category is a cluster of genes. The genes are separated into clusters by their level of variability.
    """

    bioc = "pathVar"

    version("1.32.0", commit="676c11101b513c26c199db30e7e7d33defb624c6")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-emt", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-matching", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
