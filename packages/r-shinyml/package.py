# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyml(RPackage):
	"""Compare Supervised Machine Learning Models Using Shiny App

	Implementation of a shiny app to easily compare supervised machine learning model performances. 
    You provide the data and configure each model parameter directly on the shiny app.  
    Different supervised learning algorithms can be tested either on Spark or H2O frameworks to suit your regression and classification tasks.
    Implementation of available machine learning models on R has been done by Lantz (2013, ISBN:9781782162148).
	"""
	
	homepage = "https://jeanbertinr.github.io/shinyMLpackage/"
	cran = "shinyML" 

	version("1.0.1", md5="fd87842491862322a200d4389c1ca93b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-shiny@1.0.3:", type=("build", "run"))
	depends_on("r-argondash", type=("build", "run"))
	depends_on("r-argonr", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-h2o", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-sparklyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
