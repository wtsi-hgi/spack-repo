# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGumboot(RPackage):
	"""Bootstrap Analyses of Sampling Uncertainty in Goodness-of-Fit
Statistics

	Uses jackknife and bootstrap methods to quantify the sampling uncertainty in goodness-of-fit statistics. Full details are in Clark et al. (2021), "The abuse of popular performance metrics in hydrologic modeling", Water Resources Research, <doi:10.1029/2020WR029001>. 
	"""
	
	cran = "gumboot" 

	version("1.0.1", md5="72905a9febf3e0c44e886676c3cbb370")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
