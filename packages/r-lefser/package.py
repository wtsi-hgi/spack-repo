# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLefser(RPackage):
    """R implementation of the LEfSE method for microbiome biomarker discovery

    lefser is an implementation in R of the popular "LDA Effect Size (LEfSe)" method for microbiome biomarker discovery. It uses the Kruskal-Wallis test, Wilcoxon-Rank Sum test, and Linear Discriminant Analysis to find biomarkers of groups and sub-groups.
    """

    homepage = "https://github.com/waldronlab/lefser"
    bioc = "lefser"

    version("1.18.0", commit="6f4a41256d3be73b6d04bdad660aee21ba212cb1")
    version("1.12.1", commit="cfb59f8cc993f2b8ea774a9d7d3f95d023983d80")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r@4:", type=("build", "run"))
    depends_on("r-coin", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
