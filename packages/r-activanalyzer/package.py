# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivanalyzer(RPackage):
	"""A 'Shiny' App to Analyze Accelerometer-Measured Daily Physical
Behavior Data

	A tool to analyse 'ActiGraph' accelerometer data and to implement 
    the use of the PROactive Physical Activity in COPD (chronic obstructive pulmonary disease) instruments. Once analysis
    is completed, the app allows to export results to .csv files and to generate
    a report of the measurement. All the configured inputs relevant for interpreting
    the results are recorded in the report. In addition to the existing 'R' packages 
    that are fully integrated with the app, the app uses some functions from the 
    'actigraph.sleepr' package developed by Petkova (2021) <https://github.com/dipetkov/actigraph.sleepr/>.
	"""
	
	homepage = "https://pydemull.github.io/activAnalyzer/"
	cran = "activAnalyzer" 

	version("2.0.2", md5="888fbd14cefb8887e90064bacd4f0d96")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dbplyr@2.1.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-flextable@0.8.2:", type=("build", "run"))
	depends_on("r-forcats@0.5.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-golem@0.3.4:", type=("build", "run"))
	depends_on("r-hms@1.1.2:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-modelr@0.1.9:", type=("build", "run"))
	depends_on("r-patchwork@1.1.2:", type=("build", "run"))
	depends_on("r-physicalactivity", type=("build", "run"))
	depends_on("r-plyr@1.8.7:", type=("build", "run"))
	depends_on("r-reactable@0.3:", type=("build", "run"))
	depends_on("r-rmarkdown@2.16:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
	depends_on("r-shinycssloaders@1:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.2:", type=("build", "run"))
	depends_on("r-shinydashboardplus@2.0.3:", type=("build", "run"))
	depends_on("r-shinyfeedback@0.4:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-tidyr@1.2.1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
