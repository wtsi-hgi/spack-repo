# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyrTs(RPackage):
	"""The Time Series Modeling Companion to 'healthyR'

	
    Hospital time series data analysis workflow tools, modeling, and automations. 
    This library provides many useful tools to review common administrative time 
    series hospital data. Some of these include average length of stay, and 
    readmission rates. The aim is to provide a simple and consistent verb 
    framework that takes the guesswork out of everything.
	"""
	
	homepage = "https://github.com/spsanderson/healthyR.ts"
	cran = "healthyR.ts" 

	version("0.3.0", md5="0ce241f9ed7fb7d89da5d30f14fbaf7f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-timetk", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-modeltime", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-workflowsets", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
