# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REeaaq(RPackage):
	"""Handle Air Quality Data from the European Environment Agency
Data Portal

	This software downloads and manages air quality data at the European level from the 
  European Environmental Agency (EEA) dataflows (<https://www.eea.europa.eu/data-and-maps/data/aqereporting-9>). 
	The package allows dynamically mapping the stations, summarising and time aggregating the measurements and building 
	spatial interpolation maps.
	See the webpage <https://www.eea.europa.eu/en> for further information on EEA's activities and history.
	"""
	
	cran = "EEAaq" 

	version("0.0.3", md5="71f3e0d39141bf7a0ef84d7123a50ebd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-mondate", type=("build", "run"))
	depends_on("r-aweek", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gifski", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
