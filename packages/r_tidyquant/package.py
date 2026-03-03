# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyquant(RPackage):
	"""Tidy Quantitative Financial Analysis

	Bringing business and financial analysis to the 'tidyverse'. The 'tidyquant' 
    package provides a convenient wrapper to various 'xts', 'zoo', 'quantmod', 'TTR' 
    and 'PerformanceAnalytics' package 
    functions and returns the objects in the tidy 'tibble' format. The main 
    advantage is being able to use quantitative functions with the 'tidyverse'
    functions including 'purrr', 'dplyr', 'tidyr', 'ggplot2', 'lubridate', etc. See 
    the 'tidyquant' website for more information, documentation and examples.
	"""
	
	homepage = "https://github.com/business-science/tidyquant"
	cran = "tidyquant" 

	version("1.0.7", md5="e7f122eff4ccf96b115dc391a966c066")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-quantmod@0.4.13:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-quandl", type=("build", "run"))
	depends_on("r-riingo", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-alphavantager@0.1.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-timetk@2.4:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
