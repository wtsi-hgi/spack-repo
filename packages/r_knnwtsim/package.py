# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnnwtsim(RPackage):
	"""K Nearest Neighbor Forecasting with a Tailored Similarity Metric

	Functions to implement K Nearest Neighbor forecasting using a weighted similarity metric tailored to the problem of forecasting univariate time series where recent observations, seasonal patterns, and exogenous predictors are all relevant in predicting future observations of the series in question. For more information on the formulation of this similarity metric please see Trupiano (2021) <arXiv:2112.06266>.
	"""
	
	homepage = "https://github.com/mtrupiano1/knnwtsim"
	cran = "knnwtsim" 

	version("1.0.0", md5="ccef2c2b4bd8c2f7cdd4ca269cab9788")

	depends_on("r@2.10:", type=("build", "run"))
