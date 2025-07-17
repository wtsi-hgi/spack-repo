# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenstat(RPackage):
    """Statistical analysis of phenotypic data

    Package contains methods for statistical analysis of phenotypic data.
    """

    bioc = "PhenStat"

    version("2.44.0", commit="2aa17ff94e259afc2de5aa937dcb66f4aa57171c")
    version("2.38.0", commit="806485eb5ff94c5cd26415d3d561099f837fc11b")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-smoothwin", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-nlme", type=("build", "run"))
    depends_on("r-nortest", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-msgps", type=("build", "run"))
    depends_on("r-logistf", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-pingr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
