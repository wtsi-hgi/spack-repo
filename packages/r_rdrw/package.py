# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdrw(RPackage):
	"""Univariate and Multivariate Damped Random Walk Processes

	We provide a toolbox to fit and simulate a univariate or multivariate damped random walk process that is also known as an Ornstein-Uhlenbeck process or a continuous-time autoregressive model of the first order, i.e., CAR(1) or CARMA(1, 0). This process is suitable for analyzing univariate or multivariate time series data with irregularly-spaced observation times and heteroscedastic measurement errors. When it comes to the multivariate case, the number of data points (measurements/observations) available at each observation time does not need to be the same, and the length of each time series can vary. The number of time series data sets that can be modeled simultaneously is limited to ten in this version of the package. We use Kalman-filtering to evaluate the resulting likelihood function, which leads to a scalable and efficient computation in finding maximum likelihood estimates of the model parameters or in drawing their posterior samples. Please pay attention to loading the data if this package is used for astronomical data analyses; see the details in the manual. Also see Hu and Tak (2020) <arXiv:2005.08049>.
	"""
	
	cran = "Rdrw" 

	version("1.0.2", md5="e9d137a15aea23404e06182ad6a3bd47")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.11:", type=("build", "run"))
