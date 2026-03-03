# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimetk(RPackage):
	"""A Tool Kit for Working with Time Series

	
    Easy visualization, wrangling, and feature engineering of time series data for 
    forecasting and machine learning prediction. Consolidates and extends time series functionality 
    from packages including 'dplyr', 'stats', 'xts', 'forecast', 'slider', 'padr', 'recipes', and 'rsample'.
	"""
	
	homepage = "https://github.com/business-science/timetk"
	cran = "timetk" 

	version("2.9.0", md5="17fb13250486595ae91e286e8d0eb853")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-recipes@1.0.4:", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-padr@0.5.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-readr@1.3:", type=("build", "run"))
	depends_on("r-stringi@1.4.6:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-xts@0.9.7:", type=("build", "run"))
	depends_on("r-zoo@1.7.14:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-slider", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-tsfeatures", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
