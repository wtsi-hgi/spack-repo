# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrtdstidal(RPackage):
	"""Weighted Regression for Water Quality Evaluation in Tidal Waters

	An adaptation for estuaries (tidal waters) of weighted regression
    on time, discharge, and season to evaluate trends in water quality time series. 
    Please see Beck and Hagy (2015) <doi:10.1007/s10666-015-9452-8> for 
    details.
	"""
	
	cran = "WRTDStidal" 

	version("1.1.4", md5="0565eaef2a715481d3b0b6691303baa9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
