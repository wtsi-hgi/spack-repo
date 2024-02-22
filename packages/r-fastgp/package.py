# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastgp(RPackage):
	"""Efficiently Using Gaussian Processes with Rcpp and RcppEigen

	Contains Rcpp and RcppEigen implementations of matrix operations useful for Gaussian process models, such as the inversion of a symmetric Toeplitz matrix, sampling from multivariate normal distributions, evaluation of the log-density of a multivariate normal vector, and Bayesian inference for latent variable Gaussian process models with elliptical slice sampling (Murray, Adams, and MacKay 2010).
	"""
	
	cran = "FastGP" 

	version("1.2", md5="e8e3e16939896e50c841d248ead6fbf9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rbenchmark", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
