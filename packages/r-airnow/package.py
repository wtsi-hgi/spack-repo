# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirnow(RPackage):
	"""Retrieve 'AirNow' Air Quality Observations and Forecasts

	Retrieve air quality data via the 'AirNow'
    <https://www.airnow.gov/> API.
	"""
	
	homepage = "https://github.com/briandconnelly/airnow"
	cran = "airnow" 

	version("0.1.0", md5="231642f32fba578244c4174f31f8b37f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
