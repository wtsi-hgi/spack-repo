# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStability(RPackage):
	"""Stability Analysis of Genotype by Environment Interaction (GEI)

	Functionalities to perform Stability Analysis of Genotype by Environment Interaction (GEI) to identify superior and stable genotypes under diverse environments. It performs Eberhart & Russel's ANOVA (1966) (<doi:10.2135/cropsci1966.0011183X000600010011x>), Finlay and Wilkinson (1963) Joint Linear Regression (<doi:10.1071/AR9630742>), Wricke (1962, 1964) Ecovalence, Shukla's stability variance parameter (1972) (<doi:10.1038/hdy.1972.87>)  and Kang's (1991) (<doi:10.2134/agronj1991.00021962008300010037x>) simultaneous selection for high yielding and stable parameter.
	"""
	
	homepage = "https://github.com/myaseen208/stability"
	cran = "stability" 

	version("0.5.0", md5="f49a3052aa049dc10b73c325b86706b5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
