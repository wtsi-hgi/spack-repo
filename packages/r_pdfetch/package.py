# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdfetch(RPackage):
	"""Fetch Economic and Financial Time Series Data from Public
Sources

	Download economic and financial time series from public sources, 
  including the St Louis Fed's FRED system, Yahoo Finance, the US Bureau of Labor Statistics, 
  the US Energy Information Administration, the World Bank, Eurostat, the European Central Bank,
  the Bank of England, the UK's Office of National Statistics, Deutsche Bundesbank, and INSEE.
	"""
	
	homepage = "https://github.com/abielr/pdfetch"
	cran = "pdfetch" 

	version("0.2.9", md5="a853c67045305461c68d85772d36ae09")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
