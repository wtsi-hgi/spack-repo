# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtrader(RPackage):
	"""'ETRADE' API Interface for R

	Use R to interface with the 'ETRADE' API <https://developer.etrade.com/home>.
    Functions include authentication, trading, quote requests, account information, and option 
    chains. A user will need an ETRADE brokerage account and 'ETRADE' API approval. See README 
    for authentication process and examples.
	"""
	
	homepage = "https://exploringfinance.github.io/etrader/"
	cran = "etrader" 

	version("0.1.5", md5="1a7f1c2b47b0efbff7e264d06e7a91db")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
