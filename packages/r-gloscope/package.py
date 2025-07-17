# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGloscope(RPackage):
    """Population-level Representation on scRNA-Seq data

    This package aims at representing and summarizing the entire single-cell profile of a sample. It allows researchers to perform important bioinformatic analyses at the sample-level such as visualization and quality control. The main functions Estimate sample distribution and calculate statistical divergence among samples, and visualize the distance matrix through MDS plots.
    """

    bioc = "GloScope"

    version("1.6.0", commit="055663039c2d1f340a7c23c500de695b66c6657e")
    version("1.0.0", commit="2e528517256d510e3ed60c4e6e83d4f169b8432f")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rann", type=("build", "run"))
    depends_on("r-fnn", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-mvnfast", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
