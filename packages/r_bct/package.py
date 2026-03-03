# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBct(RPackage):
	"""Bayesian Context Trees for Discrete Time Series

	An implementation of a collection of tools for exact Bayesian inference with discrete times series. This package contains functions that can be used for prediction, model selection, estimation, segmentation/change-point detection and other statistical tasks. Specifically, the functions provided can be used for the exact computation of the prior predictive likelihood of the data, for the identification of the a posteriori most likely (MAP) variable-memory Markov models, for calculating the exact posterior probabilities and the AIC and BIC scores of these models, for prediction with respect to log-loss and 0-1 loss and segmentation/change-point detection. Example data sets from finance, genetics, animal communication and meteorology are also provided. Detailed descriptions of the underlying theory and algorithms can be found in [Kontoyiannis et al. 'Bayesian Context Trees: Modelling and exact inference for discrete time series.' Journal of the Royal Statistical Society: Series B (Statistical Methodology), April 2022. Available at: <arXiv:2007.14900> [stat.ME], July 2020] and [Lungu et al. 'Change-point Detection and Segmentation of Discrete Data using Bayesian Context Trees' <arXiv:2203.04341> [stat.ME], March 2022]. 
	"""
	
	cran = "BCT" 

	version("1.2", md5="f8906a787090a5a05ba14700bcace59a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
