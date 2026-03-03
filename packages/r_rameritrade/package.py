# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRameritrade(RPackage):
	"""'TD Ameritrade' API Interface for R

	Use R to interface with the 'TD Ameritrade' API <https://developer.tdameritrade.com/>.
    Functions include authentication, trading, price requests, account information, and option 
    chains. A user will need a TD brokerage account and TD Ameritrade developer app. See README 
    for authentication process and examples.
	"""
	
	homepage = "https://exploringfinance.github.io/rameritrade/"
	cran = "rameritrade" 

	version("0.1.5", md5="48a6da442145782aed89107b30a5741d")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-urltools@1.7.3:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
