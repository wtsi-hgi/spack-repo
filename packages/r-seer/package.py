# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeer(RPackage):
	"""Feature-Based Forecast Model Selection

	A novel meta-learning framework for forecast model selection using time series features. Many applications require a large number of time series to be forecast. Providing better forecasts for these time series is important in decision and policy making. We propose a classification framework which selects forecast models based on features calculated from the time series. We call this framework FFORMS (Feature-based FORecast Model Selection). FFORMS builds a mapping that relates the features of time series to the best forecast model using a random forest. 'seer' package is the implementation of the FFORMS algorithm. For more details see our paper at <https://www.monash.edu/business/econometrics-and-business-statistics/research/publications/ebs/wp06-2018.pdf>.
	"""
	
	homepage = "https://thiyangt.github.io/seer/"
	cran = "seer" 

	version("1.1.8", md5="b9cb12746d524998effedd0f1789146c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-forecast@8.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-forectheta", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-tsfeatures", type=("build", "run"))
