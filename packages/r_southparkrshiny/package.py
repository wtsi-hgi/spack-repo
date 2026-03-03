# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSouthparkrshiny(RPackage):
	"""Data and 'Shiny' Application for the Show 'SouthPark'

	Ratings, votes, swear words and sentiments are analysed for
    the show 'SouthPark' through a 'Shiny' application after web scraping 
    from 'IMDB' and the website <https://southpark.fandom.com/wiki/South_Park_Archives>.
	"""
	
	homepage = "https://github.com/Amalan-ConStat/SouthParkRshiny"
	cran = "SouthParkRshiny" 

	version("1.0.0", md5="946f059f4e76315459238ea6ba1516d1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-box", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-config@0.3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-golem@0.4.1:", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-shiny@1.8:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
