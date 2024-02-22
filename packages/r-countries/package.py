# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountries(RPackage):
	"""Deal with Country Data in an Easy Way

	Wrangle country data more effectively and quickly. 
    This package contains functions to easily identify and convert country names,
    download country information, merge country data from different sources, 
    and make quick world maps.
	"""
	
	homepage = "https://fbellelli.github.io/countries/"
	cran = "countries" 

	version("1.2.0", md5="a93738a0d48e33ea1043d4152eacb36d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
