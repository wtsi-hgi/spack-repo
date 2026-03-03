# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaqgetr(RPackage):
	"""Import Air Quality Monitoring Data in a Fast and Easy Way

	A collection of tools to access prepared air quality monitoring
    data files from web servers with ease and speed. Air quality data are 
    sourced from open and publicly accessible repositories and can be found in 
    these locations: 
    <https://www.eea.europa.eu/data-and-maps/data/airbase-the-european-air-quality-database-8> 
    and <https://discomap.eea.europa.eu/map/fme/AirQualityExport.htm>. The web 
    server space has been provided by Ricardo Energy & Environment.
	"""
	
	homepage = "https://github.com/skgrange/saqgetr"
	cran = "saqgetr" 

	version("0.2.21", md5="e073a128a7f7f9e8608bc0f3e3189c57")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
