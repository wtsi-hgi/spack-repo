# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpencage(RPackage):
	"""Geocode with the OpenCage API

	Geocode with the OpenCage API, either from place name to longitude 
    and latitude (forward geocoding) or from longitude and latitude to the name 
    and address of a location (reverse geocoding), see 
    <https://opencagedata.com/>.
	"""
	
	homepage = "https://docs.ropensci.org/opencage/"
	cran = "opencage" 

	version("0.2.2", md5="886ab9d0978188509c242b51445c6001")

	depends_on("r-crul@0.5.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-memoise@1.1:", type=("build", "run"))
	depends_on("r-progress@1.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-ratelimitr@0.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-withr@2:", type=("build", "run"))
