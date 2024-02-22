# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsplinepsd(RPackage):
	"""Bayesian Nonparametric Spectral Density Estimation Using
B-Spline Priors

	Implementation of a Metropolis-within-Gibbs MCMC algorithm to flexibly estimate the spectral density of a stationary time series.  The algorithm updates a nonparametric B-spline prior using the Whittle likelihood to produce pseudo-posterior samples and is based on the work presented in Edwards, M.C., Meyer, R. and Christensen, N., Statistics and Computing (2018). <doi.org/10.1007/s11222-017-9796-9>.
	"""
	
	cran = "bsplinePsd" 

	version("0.6.0", md5="b5162ab6018c950a73df03e50008ad8c")

	depends_on("r-rcpp", type=("build", "run"))
