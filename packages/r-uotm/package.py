# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUotm(RPackage):
	"""Uncertainty of Time Series Model Selection Methods

	We propose a new procedure, called model uncertainty variance, which can quantify the uncertainty of model selection on Autoregressive Moving Average models. The model uncertainty variance not pay attention to the accuracy of prediction, but focus on model selection uncertainty and providing more information of the model selection results. And to estimate the model measures, we propose an simplify and faster algorithm based on bootstrap method, which is proven to be effective and feasible by Monte-Carlo simulation. At the same time, we also made some optimizations and adjustments to the Model Confidence Bounds algorithm, so that it can be applied to the time series model selection method. The consistency of the algorithm result is also verified by Monte-Carlo simulation. We propose a new procedure, called model uncertainty variance, which can quantify the uncertainty of model selection on Autoregressive Moving Average models. The model uncertainty variance focuses on model selection uncertainty and providing more information of the model selection results. To estimate the model uncertainty variance, we propose an simplified and faster algorithm based on bootstrap method, which is proven to be effective and feasible by Monte-Carlo simulation. At the same time, we also made some optimizations and adjustments to the Model Confidence Bounds algorithm, so that it can be applied to the time series model selection method. The consistency of the algorithm result is also verified by Monte-Carlo simulation. Please see Li,Y., Luo,Y., Ferrari,D., Hu,X. and Qin,Y. (2019) Model Confidence Bounds for Variable Selection. Biometrics, 75:392-403.<DOI:10.1111/biom.13024> for more information.
	"""
	
	cran = "uotm" 

	version("0.1.6", md5="aec4baea6c9618ea7b00af5337f570b2")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
