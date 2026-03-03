# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBawir(RPackage):
	"""Analysis of Basketball Data

	Collection of tools to work with European basketball data. Functions available are related to friendly 
	web scraping, data management and visualization. Data were obtained from <https://www.euroleaguebasketball.net/euroleague/>, 
	<https://www.euroleaguebasketball.net/eurocup/> and <https://www.acb.com/>, following the instructions 
        of their respectives robots.txt files, when available. Box score data are available for the three leagues. 
	Play-by-play data are also available for the Spanish league. Methods for analysis include a population pyramid, 
	2D plots, circular plots of players' percentiles, plots of players' monthly/yearly stats, team heatmaps, 
	team shooting plots, team four factors plots, cross-tables with the results of regular season games,
	maps of nationalities, combinations of lineups, possessions-related variables, timeouts,
	performance by periods, personal fouls and offensive rebounds. 
	Please see Vinue (2020) <doi:10.1089/big.2018.0124>. 
	"""
	
	homepage = "https://www.uv.es/vivigui/basketball_platform.html"
	cran = "BAwiR" 

	version("1.3.2", md5="ad75617b55b703ab77a6e7c68bc41d09")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-anthropometry", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-rworldmap", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
