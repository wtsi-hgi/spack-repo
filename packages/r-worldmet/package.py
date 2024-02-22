# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorldmet(RPackage):
	"""Import Surface Meteorological Data from NOAA Integrated Surface
Database (ISD)

	Functions to import data from more than 30,000 surface
    meteorological sites around the world managed by the National Oceanic and Atmospheric Administration (NOAA) Integrated Surface
    Database (ISD).
	"""
	
	homepage = "https://davidcarslaw.github.io/worldmet/index.html"
	cran = "worldmet" 

	version("0.9.8", md5="9214798fb728ec09b9081a7da83b5eee")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
