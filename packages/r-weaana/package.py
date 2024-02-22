# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeaana(RPackage):
	"""Analysis the Weather Data

	Functions are collected to analyse weather data for agriculture 
    purposes including to read weather records in multiple formats, 
    calculate extreme climate index.
	"""
	
	homepage = "https://weaana.bangyou.me/"
	cran = "weaana" 

	version("0.1.1", md5="ac4b7f456e38e3564cbad3d70be95d2b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
