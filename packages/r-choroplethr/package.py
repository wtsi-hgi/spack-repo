# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoroplethr(RPackage):
	"""Simplify the Creation of Choropleth Maps in R

	Choropleths are thematic maps where geographic regions, such as
    states, are colored according to some metric, such as the number of people
    who live in that state. This package simplifies this process by 1.
    Providing ready-made functions for creating choropleths of common maps. 2.
    Providing data and API connections to interesting data sources for making
    choropleths. 3. Providing a framework for creating choropleths from
    arbitrary shapefiles. 4. Overlaying those maps over reference maps from
    Google Maps. 
	"""
	
	homepage = "www.choroplethr.com"
	cran = "choroplethr" 

	version("3.7.3", md5="2012a42f97fc8b3a407b84056a8b62a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-acs", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-wdi", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-rgooglemaps", type=("build", "run"))
	depends_on("r-tigris@1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidycensus", type=("build", "run"))
