# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWildviz(RPackage):
	"""Compiles and Visualizes Wildfire, Climate, and Air Quality Data

	Fetches data from three disparate data sources and allows user to perform analyses on them. It offers two core components: 1. A robust data retrieval and preparation infrastructure for wildfire, climate, and air quality index data and 2. A simple, informative, and interactive visualizations of the aforementioned datasets for California counties from 2011 through 2015. The sources of data are: wildfire data from Kaggle <https://www.kaggle.com/rtatman/188-million-us-wildfires>, climate data from the National Oceanic and Atmospheric Administration  <https://www.ncdc.noaa.gov/cdo-web/token>, and air quality data from the Environmental Protection Agency <https://aqs.epa.gov/aqsweb/documents/data_api.html>. 
	"""
	
	homepage = "https://github.com/bradraff/wildviz"
	cran = "wildviz" 

	version("0.1.2", md5="31dccc0d2044131bda04c08acfb6eec3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rnoaa", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
