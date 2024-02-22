# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipcoder(RPackage):
	"""Data & Functions for Working with US ZIP Codes

	Make working with ZIP codes in R painless with an integrated dataset of U.S. ZIP codes and functions for working with them. 
             Search ZIP codes by multiple geographies, including state, county, city & across time zones. Also included are functions for relating
             ZIP codes to Census data, geocoding & distance calculations.
	"""
	
	homepage = "https://github.com/gavinrozzi/zipcodeR/"
	cran = "zipcodeR" 

	version("0.3.5", md5="ab122c93022d59e4aaebb3f5a1c7df7e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-tidycensus", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
