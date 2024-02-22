# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesarimax(RPackage):
	"""Bayesian Estimation of ARIMAX Model

	The Autoregressive Integrated Moving Average (ARIMA) model is very popular univariate time series model. Its application has been widened by the incorporation of exogenous variable(s) (X) in the model and modified as ARIMAX by Bierens (1987) <doi:10.1016/0304-4076(87)90086-8>. In this package we estimate the ARIMAX model using Bayesian framework. 
	"""
	
	cran = "BayesARIMAX" 

	version("0.1.1", md5="77da4c5cdd11d5cc7e7043c8506d95e3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
