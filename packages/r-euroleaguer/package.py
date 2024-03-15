# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REuroleaguer(RPackage):
	"""'Euroleague basketball API'

	Unofficial API wrapper for 'Euroleague' and 'Eurocup' basketball API (<https://www.euroleaguebasketball.net/en/euroleague/>), it allows to retrieve real-time and historical standard and advanced statistics about competitions, teams, players and games.
	"""
	
	homepage = "https://github.com/FlavioLeccese92/euroleaguer/"
	cran = "euroleaguer" 

	version("0.2.0", md5="ad22afa061028402528e650ebabc9897")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
