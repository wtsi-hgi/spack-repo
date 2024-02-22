# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutots(RPackage):
	"""Automatic Model Selection and Prediction for Univariate Time
Series

	Offers a set of functions to easily make predictions for univariate time series. 
             'autoTS' is a wrapper of existing functions of the 'forecast' and 'prophet' packages, 
             harmonising their outputs in tidy dataframes and using default values for each.
             The core function getBestModel() allows the user to effortlessly benchmark seven 
             algorithms along with a bagged estimator to identify which one performs the best 
             for a given time series.
	"""
	
	homepage = "https://github.com/vivienroussez/autoTS"
	cran = "autoTS" 

	version("0.9.11", md5="30d4aaf81027638e1e0045c3bdb7ef83")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-prophet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
