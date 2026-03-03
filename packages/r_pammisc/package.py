# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPammisc(RPackage):
	"""Miscellaneous Functions for Passive Acoustic Analysis

	A collection of miscellaneous functions for passive acoustics. 
    Much of the content here is adapted to R from code written by other people.
    If you have any ideas of functions to add, please contact Taiki Sakai.
	"""
	
	cran = "PAMmisc" 

	version("1.11.6", md5="045a0b4632cc7f2cc6c0e6092cddaf7a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-pambinaries", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rerddap", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-hoardr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
