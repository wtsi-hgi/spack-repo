# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasstr(RPackage):
	"""Analyze, Summarize, and Visualize Daily Streamflow Data

	The Flow Analysis Summary Statistics Tool for R, 'fasstr', provides various functions to tidy and screen daily stream discharge data, calculate and visualize various summary statistics and metrics, and compute annual trending and volume frequency analyses. 
     It features useful function arguments for filtering of and handling dates, customizing data and metrics, and the ability to pull daily data directly from the Water Survey of Canada hydrometric database (<https://collaboration.cmc.ec.gc.ca/cmc/hydrometrics/www/>).
	"""
	
	homepage = "https://bcgov.github.io/fasstr/"
	cran = "fasstr" 

	version("0.5.1", md5="c93b56cacaf94a7818915125cede3903")
	version("0.5.2", md5="735f7933ee71f86041cd086a9784d207")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-e1071@1.7.0.1:", type=("build", "run"))
	depends_on("r-fitdistrplus@1.0.14:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-openxlsx@4.1:", type=("build", "run"))
	depends_on("r-pearsonds@1.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rcpproll@0.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-tidyhydat@0.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-zyp@0.10.1.1:", type=("build", "run"))
