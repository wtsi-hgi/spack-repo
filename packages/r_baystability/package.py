# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaystability(RPackage):
	"""Bayesian Stability Analysis of Genotype by Environment
Interaction (GEI)

	Performs general Bayesian estimation method of linear–bilinear models for genotype × environment interaction. The method is explained in Perez-Elizalde, S., Jarquin, D., and Crossa, J. (2011) (<doi:10.1007/s13253-011-0063-9>).
	"""
	
	cran = "baystability" 

	version("0.1.0", md5="c8bd81c5fc7cedc365fff35f01ed0ce2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstiefel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
