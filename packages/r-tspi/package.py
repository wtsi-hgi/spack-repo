# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTspi(RPackage):
	"""Improved Prediction Intervals for ARIMA Processes and Structural
Time Series

	Prediction intervals for ARIMA and structural time series
    models using importance sampling approach with uninformative priors for model
    parameters, leading to more accurate coverage probabilities in frequentist
    sense. Instead of sampling the future observations and hidden states of the
    state space representation of the model, only model parameters are sampled,
    and the method is based solving the equations corresponding to the conditional
    coverage probability of the prediction intervals. This makes method relatively
    fast compared to for example MCMC methods, and standard errors of prediction
    limits can also be computed straightforwardly.
	"""
	
	cran = "tsPI" 

	version("1.0.4", md5="8f35e323eb48a443a71b86f035acf30b")

	depends_on("r-kfas", type=("build", "run"))
