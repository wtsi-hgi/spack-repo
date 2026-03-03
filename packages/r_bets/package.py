# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBets(RPackage):
	"""Brazilian Economic Time Series

	It provides access to and information about the most important
    Brazilian economic time series - from the Getulio Vargas Foundation <http://portal.fgv.br/en>,
    the Central Bank of Brazil <http://www.bcb.gov.br> and the Brazilian Institute of Geography
    and Statistics <http://www.ibge.gov.br>. It also presents tools for managing, analysing (e.g.
    generating dynamic reports with a complete analysis of a series) and exporting
    these time series.
	"""
	
	homepage = "https://github.com/nmecsys/BETS"
	cran = "BETS" 

	version("0.4.9", md5="4358cec246a72e5b00f446924a4d3790")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-grnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-seasonal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
