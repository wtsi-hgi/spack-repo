# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBitmexr(RPackage):
	"""R Client for BitMEX

	A client for cryptocurrency exchange BitMEX
    <https://www.bitmex.com/> including the ability to obtain historic
    trade data and place, edit and cancel orders. BitMEX's Testnet and
    live API are both supported.
	"""
	
	homepage = "https://github.com/hfshr/bitmexr/"
	cran = "bitmexr" 

	version("0.3.3", md5="521ed2c26199346af1b065b61b9fdbd7")

	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
