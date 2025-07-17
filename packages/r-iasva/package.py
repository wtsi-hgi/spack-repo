# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIasva(RPackage):
    """Iteratively Adjusted Surrogate Variable Analysis

    Iteratively Adjusted Surrogate Variable Analysis (IA-SVA) is a statistical framework to uncover hidden sources of variation even when these sources are correlated. IA-SVA provides a flexible methodology to i) identify a hidden factor for unwanted heterogeneity while adjusting for all known factors; ii) test the significance of the putative hidden factor for explaining the unmodeled variation in the data; and iii), if significant, use the estimated factor as an additional known factor in the next iteration to uncover further hidden factors.
    """

    bioc = "iasva"

    version("1.26.0", commit="bc67c5391d4244f2da7c8d6cf5e047d8c4751a66")
    version("1.20.0", commit="e6e4472fbb67315324db2c5a3060f8b3e23c86bb")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
