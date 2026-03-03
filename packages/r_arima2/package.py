# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArima2(RPackage):
	"""Likelihood Based Inference for ARIMA Modeling

	Estimating and analyzing auto regressive integrated moving average
    (ARIMA) models. The primary function in this package is arima(), which fits 
    an ARIMA model to univariate time series data using a random restart
    algorithm. This approach frequently leads to models that have model 
    likelihood greater than or equal to that of the likelihood obtained by 
    fitting the same model using the arima() function from the 'stats' package. 
    This package enables proper optimization of model likelihoods, which is a 
    necessary condition for performing likelihood ratio tests. This package 
    relies heavily on the source code of the arima() function of the 'stats' 
    package. For more information, please see Jesse Wheeler and Edward L. 
    Ionides (2023) <arXiv:2310.01198>.
	"""
	
	cran = "arima2" 

	version("3.1.0", md5="d31c977a3227f7d0bc9d1a6c670c7b4f", url="https://cran.r-project.org/src/contrib/arima2_3.1.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
