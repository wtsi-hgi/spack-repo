# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwitterautomatedtrading(RPackage):
	"""Automated Trading Using Tweets

	Provides an integration to the 'metatrader 5'. 
    The functionalities carry out automated trading using
    sentiment indexes computed from 'twitter' and/or 'stockwits'. 
    The sentiment indexes are based on the ph.d. dissertation 
    "Essays on Economic Forecasting Models" (Godeiro,2018) <https://repositorio.ufpb.br/jspui/handle/123456789/15198>
    The integration between the 'R' and the 'metatrader 5' allows sending buy/sell orders to the brokerage. 
	"""
	
	homepage = "https://github.com/lucasgodeiro/TwitterAutomatedTrading"
	cran = "TwitterAutomatedTrading" 

	version("0.1.0", md5="032ce4c270eb6ef41249fbaa7462d7ff")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-twitter", type=("build", "run"))
	depends_on("r-naptime", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
