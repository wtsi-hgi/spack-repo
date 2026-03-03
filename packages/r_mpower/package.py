# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpower(RPackage):
	"""Power Analysis via Monte Carlo Simulation for Correlated Data

	A flexible framework for power analysis using Monte
    Carlo simulation for settings in which considerations of the correlations
    between predictors are important. Users can set up a data generative model
    that preserves dependence structures among predictors given existing data
    (continuous, binary, or ordinal). Users can also generate power curves to
    assess the trade-offs between sample size, effect size, and power of a design.
    This package includes several statistical models common in environmental
    mixtures studies. For more details and tutorials, see Nguyen et al. (2022) <arXiv:2209.08036>.
	"""
	
	cran = "mpower" 

	version("0.1.0", md5="5a907408dc26b2b65897cafc34131c48")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-sbgcop", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
