# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKalmanfilter(RPackage):
	"""Kalman Filter

	'Rcpp' implementation of the multivariate Kalman filter for state space models that can handle missing values and exogenous data in the observation and state equations. There is also a function to handle time varying parameters.
  Kim, Chang-Jin and Charles R. Nelson (1999) "State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Applications" <doi:10.7551/mitpress/6444.001.0001><http://econ.korea.ac.kr/~cjkim/>. 
	"""
	
	cran = "kalmanfilter" 

	version("2.1.0", md5="ec3cd237ccf0a1e84e81a02a7358d829")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
