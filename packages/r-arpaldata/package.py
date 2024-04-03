# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArpaldata(RPackage):
	"""Retrieving and Analyzing Air Quality and Weather Data from ARPA
Lombardia

	Contains functions for retrieving, managing and analysing air quality and weather data from Regione Lombardia open database (<https://www.dati.lombardia.it/>).
    Data are collected by ARPA Lombardia (Lombardia Environmental Protection Agency), Italy, through its ground monitoring network.
    See the webpage <https://www.arpalombardia.it/> for further information on ARPA Lombardia's activities and history.
    Data quality (e.g. missing values, exported values, graphical mapping) has been checked involving members of the ARPA Lombardia's office for air quality control.
    The package makes available observations since 1989 (for weather) and 1968 (for air quality) and are updated with daily frequency by the regional agency.
    Full description of the package can be retrieved in the companion paper Maranzano & Algieri (2024), "ARPALData: an R package for retrieving and analyzing air quality 
    and weather data from ARPA Lombardia (Italy)", Environmental and Ecological Statistics, <doi:10.1007/s10651-024-00599-6>.
	"""
	
	cran = "ARPALData" 

	version("1.5.1", md5="bad7deb37b648b7b655a0e753fd5138a")
	version("1.5.2", md5="d7b81ce7e24b7b024b498a034dccf29a")

	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-eurostat", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-aweek", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-archive", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
