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
	"""
	
	cran = "ARPALData" 

	version("1.5.0", md5="69f58c643c3355d0cdeb08eab1392de0")

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
