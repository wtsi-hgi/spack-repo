# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForecastml(RPackage):
	"""Time Series Forecasting with Machine Learning Methods

	The purpose of 'forecastML' is to simplify the process of multi-step-ahead forecasting with standard machine learning algorithms. 'forecastML' supports lagged, dynamic, static, and grouping features for modeling single and grouped numeric or factor/sequence time series. In addition, simple wrapper functions are used to support model-building with most R packages. This approach to forecasting is inspired by Bergmeir, Hyndman, and Koo's (2018) paper "A note on the validity of cross-validation for evaluating autoregressive time series prediction" <doi:10.1016/j.csda.2017.11.003>.
	"""
	
	homepage = "https://github.com/nredell/forecastML/"
	cran = "forecastML" 

	version("0.9.0", md5="bfc792a1b9cd76c9e19b94251c50d2e6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-future-apply@1.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
	depends_on("r-dtplyr@1:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
