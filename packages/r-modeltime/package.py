# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeltime(RPackage):
	"""The Tidymodels Extension for Time Series Modeling

	
    The time series forecasting framework for use with the 'tidymodels' ecosystem. 
    Models include ARIMA, Exponential Smoothing, and additional time series models
    from the 'forecast' and 'prophet' packages. Refer to "Forecasting Principles & Practice, Second edition" 
    (<https://otexts.com/fpp2/>).
    Refer to "Prophet: forecasting at scale" 
    (<https://research.facebook.com/blog/2017/02/prophet-forecasting-at-scale/>.).
	"""
	
	homepage = "https://github.com/business-science/modeltime"
	cran = "modeltime" 

	version("1.2.8", md5="47ab6baed869415fc194f76f2f4d6e5e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stanheaders", type=("build", "run"))
	depends_on("r-timetk@2.8.1:", type=("build", "run"))
	depends_on("r-parsnip@0.2.1:", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-yardstick@0.0.8:", type=("build", "run"))
	depends_on("r-workflows@1:", type=("build", "run"))
	depends_on("r-hardhat@1:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-xgboost@1.2.0.1:", type=("build", "run"))
	depends_on("r-prophet", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-tidymodels", type=("build", "run"))
