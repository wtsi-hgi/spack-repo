# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarfima(RPackage):
	"""Continuous-Time Fractionally Integrated ARMA Process for
Irregularly Spaced Long-Memory Time Series Data

	We provide a toolbox to fit a continuous-time fractionally integrated ARMA process (CARFIMA) on univariate and irregularly spaced time series data via both frequentist and Bayesian machinery. A general-order CARFIMA(p, H, q) model for p>q is specified in Tsai and Chan (2005) <doi:10.1111/j.1467-9868.2005.00522.x> and it involves p+q+2 unknown model parameters, i.e., p AR parameters, q MA parameters, Hurst parameter H, and process uncertainty (standard deviation) sigma. Also, the model can account for heteroscedastic measurement errors, if the information about measurement error standard deviations is known. The package produces their maximum likelihood estimates and asymptotic uncertainties using a global optimizer called the differential evolution algorithm. It also produces posterior samples of the model parameters via Metropolis-Hastings within a Gibbs sampler equipped with adaptive Markov chain Monte Carlo. These fitting procedures, however, may produce numerical errors if p>2. The toolbox also contains a function to simulate discrete time series data from CARFIMA(p, H, q) process given the model parameters and observation times. 
	"""
	
	cran = "carfima" 

	version("2.0.2", md5="fedb387d76c0e4487c7bc79425eefbbe")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.11:", type=("build", "run"))
	depends_on("r-deoptim@2.2.5:", type=("build", "run"))
	depends_on("r-pracma@2.2.9:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
	depends_on("r-invgamma@1.1:", type=("build", "run"))
