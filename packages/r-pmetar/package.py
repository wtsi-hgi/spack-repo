# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmetar(RPackage):
	"""Processing METAR Weather Reports

	Allows to download current and historical METAR weather reports
  extract and parse basic parameters and present main weather information. 
  Current reports are downloaded from Aviation Weather Center 
  <https://aviationweather.gov/data/metar/> and historical reports from
  Iowa Environmental Mesonet web page of Iowa State University
  ASOS-AWOS-METAR <http://mesonet.agron.iastate.edu/AWOS/>.
	"""
	
	homepage = "https://github.com/prcwiek/pmetar"
	cran = "pmetar" 

	version("0.5.0", md5="c14697d8af172bda543f68165874d773")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
