# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPricer(RPackage):
	"""Economics and Pricing Tools

	Functions to aid in micro and macro economic analysis and handling of price and
    currency data. Includes extraction of relevant inflation and exchange rate data from World Bank
    API, data cleaning/parsing, and standardisation. Inflation adjustment
    calculations as found in Principles of Macroeconomics by Gregory Mankiw et al (2014). Current
    and historical end of day exchange rates for 171 currencies from the European Central Bank
    Statistical Data Warehouse (2020) <https://sdw.ecb.europa.eu/curConverter.do>.
	"""
	
	homepage = "https://github.com/stevecondylios/priceR"
	cran = "priceR" 

	version("1.0.1", md5="8bf79a75bc885297f2b7dda6bc1e0fc5")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
