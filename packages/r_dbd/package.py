# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbd(RPackage):
	"""Discretised Beta Distribution

	Tools for working with a new versatile
	discrete distribution, the db ("discretised Beta")
	distribution.  This package provides density (probability),
	distribution, inverse distribution (quantile) and random
	data generation functions for the db family.  It provides
	functions to effect conveniently maximum likelihood
	estimation of parameters, and a variety of useful plotting
	functions.  It provides goodness of fit tests and functions
	to calculate the Fisher information, different estimates of
	the hessian of the log likelihood and Monte Carlo estimation
	of the covariance matrix of the maximum likelihood parameter
	estimates.  In addition it provides analogous tools for
	working with the beta-binomial distribution which has been
	proposed as a competitor to the db distribution.
	"""
	
	cran = "dbd" 

	version("0.0-22", md5="3a92ab191501ea01e4a38a4e6ba1a189")

	depends_on("r@3.2.2:", type=("build", "run"))
