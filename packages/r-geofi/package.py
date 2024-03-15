# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeofi(RPackage):
	"""Access Finnish Geospatial Data

	Designed to simplify geospatial data access from the Statistics Finland Web Feature Service API <https://geo.stat.fi/geoserver/index.html>, the geofi package offers researchers and analysts a set of tools to obtain and harmonize administrative spatial data for a wide range of applications, from urban planning to environmental research. The package contains annually updated time series of municipality key datasets that can be used for data aggregation and language translations.
	"""
	
	homepage = "https://ropengov.github.io/geofi/"
	cran = "geofi" 

	version("1.0.15", md5="3aa42ad4b79cbc95fff1de816f0edf3e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httpcache", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
