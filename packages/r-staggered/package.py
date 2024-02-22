# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStaggered(RPackage):
	"""Efficient Estimation Under Staggered Treatment Timing

	Efficiently estimates treatment effects in settings with randomized staggered rollouts, using tools 
    proposed by Roth and Sant'Anna (2021) <arXiv:2102.01291>.
	"""
	
	cran = "staggered" 

	version("1.1", md5="a535d15174d799c88205a189f5a718aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
