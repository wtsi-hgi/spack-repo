# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGompertztrunc(RPackage):
	"""Conducting Maximum Likelihood Estimation with Truncated
Mortality Data

	Estimates hazard ratios and mortality
    differentials for doubly-truncated data without population
    denominators.
	"""
	
	homepage = "https://caseybreen.github.io/gompertztrunc/"
	cran = "gompertztrunc" 

	version("0.1.1", md5="10f8c465fc75bd491d4cf8bcd74a345d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
