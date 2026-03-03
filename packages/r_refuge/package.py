# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefuge(RPackage):
	"""Locate Trans and Intersex-Friendly Toilets

	Access the 'Refuge' API, a web-application for locating trans and 
    intersex-friendly restrooms, including unisex and accessible restrooms. 
    Includes data on the location of restrooms, along with directions, 
    comments, user ratings and amenities. Coverage is global, but data is 
    most comprehensive in the United States.
    See <https://www.refugerestrooms.org/api/docs/> for full API documentation.
	"""
	
	homepage = "https://docs.evanodell.com/refuge"
	cran = "refuge" 

	version("0.3.3", md5="2b03d244d7237b48cf5ae765c23394e9")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
