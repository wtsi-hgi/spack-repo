# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmapgeocode(RPackage):
	"""An Interface to the 'AutoNavi Maps' API Geocoding Services

	Getting and parsing data of location geocode/reverse-geocode and administrative regions from 'AutoNavi Maps'<https://lbs.amap.com/api/webservice/summary> API.
	"""
	
	homepage = "https://github.com/womeimingzi11/amapGeocode"
	cran = "amapGeocode" 

	version("0.6.0", md5="6a8096b4eacb2d826582a74225e6fe60")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
