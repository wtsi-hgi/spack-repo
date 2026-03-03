# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNjgeo(RPackage):
	"""Tools for Geocoding Addresses in New Jersey using the 'NJOGIS'
API

	Provides an R interface to free geocoding REST APIs maintained by the New Jersey Office of GIS <https://njgin.nj.gov/njgin/edata/geocoding/index.html#!/> and commonly used shapefiles. 
	"""
	
	cran = "njgeo" 

	version("0.1.0", md5="694fc8b8cc41a37dc96b70d1356b429d")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
