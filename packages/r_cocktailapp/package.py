# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocktailapp(RPackage):
	"""'shiny' App to Discover Cocktails

	A 'shiny' app to discover cocktails. The
    app allows one to search for cocktails by ingredient,
    filter on rating, and number of ingredients. The
    package also contains data with the ingredients of
    nearly 26 thousand cocktails scraped from the web.
	"""
	
	homepage = "https://github.com/shabbychef/cocktailApp"
	cran = "cocktailApp" 

	version("0.2.3", md5="cf436e03b120da8628a82d6f4bf8b114")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggtern", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
