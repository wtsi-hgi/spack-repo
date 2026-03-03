# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeltimeResample(RPackage):
	"""Resampling Tools for Time Series Forecasting

	
    A 'modeltime' extension that implements forecast resampling tools
    that assess time-based model performance and stability for a single time series, 
    panel data, and cross-sectional time series analysis. 
	"""
	
	homepage = "https://github.com/business-science/modeltime.resample"
	cran = "modeltime.resample" 

	version("0.2.3", md5="1c53a96d22be0c86be8794ae7a9e97f1")

	depends_on("r-modeltime@0.3:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
	depends_on("r-parsnip@0.1.4:", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
	depends_on("r-timetk@2.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
