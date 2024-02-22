# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmpcloudr(RPackage):
	"""R Access to the 'FMP Cloud' and 'Financial Modeling Prep' API

	Use R to access to the 'FMP Cloud' API <https://fmpcloud.io/> and 
    'Financial Modeling Prep' API <https://financialmodelingprep.com/developer/docs/>.
    Data available includes stock prices, market indexes, company fundamentals,
    13F holdings data, and much more. A valid API token must be set to enable
    functions. 
	"""
	
	homepage = "https://exploringfinance.github.io/fmpcloudr/"
	cran = "fmpcloudr" 

	version("0.1.5", md5="2e9b18f4a93b372ec7410f1959e4ae3e")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
