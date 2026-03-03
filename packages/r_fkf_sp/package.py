# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFkfSp(RPackage):
	"""Fast Kalman Filtering Through Sequential Processing

	Fast and flexible Kalman filtering and smoothing implementation utilizing sequential processing, designed for efficient parameter estimation through maximum likelihood estimation. Sequential processing is a univariate treatment of a multivariate series of observations and can benefit from computational efficiency over traditional Kalman filtering when independence is assumed in the variance of the disturbances of the measurement equation. Sequential processing is described in the textbook of Durbin and Koopman (2001, ISBN:978-0-19-964117-8). 'FKF.SP' was built upon the existing 'FKF' package and is, in general, a faster Kalman filter/smoother.
	"""
	
	homepage = "https://github.com/TomAspinall/FKF.SP"
	cran = "FKF.SP" 

	version("0.3.1", md5="5038e9389af5237670cda79cf360c24d")

	depends_on("r-mathjaxr", type=("build", "run"))
