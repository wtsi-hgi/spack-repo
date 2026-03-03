# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHymett(RPackage):
	"""Hydrologic Model Evaluation and Time-Series Tools

	Facilitates the analysis and evaluation of hydrologic model output and 
    time-series data with functions focused on comparison of modeled (simulated) and observed data, 
    period-of-record statistics, and trends.  
	"""
	
	homepage = "https://code.usgs.gov/hymett/hymett"
	cran = "HyMETT" 

	version("1.1.2", md5="4496272ec356194ad20a68f496472a22")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
