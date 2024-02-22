# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcessmort(RPackage):
	"""Excess Mortality

	Implementation of method for estimating excess mortality and other health related outcomes from weekly or daily count data described in Acosta and Irizarry (2021) "A Flexible Statistical Framework for Estimating Excess Mortality".
	"""
	
	cran = "excessmort" 

	version("0.6.1", md5="d9abd4475119f410f0819cbce6d84d60")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
