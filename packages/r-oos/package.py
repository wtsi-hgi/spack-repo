# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROos(RPackage):
	"""Out-of-Sample Time Series Forecasting

	A comprehensive and cohesive API for the out-of-sample forecasting workflow: 
             data preparation, forecasting - including both traditional econometric time series models and 
             modern machine learning techniques - forecast combination, model and error analysis, and 
             forecast visualization. 
	"""
	
	homepage = "https://github.com/tylerJPike/OOS"
	cran = "OOS" 

	version("1.0.0", md5="3e6ffe94046eb5b37fab624527171bd2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
