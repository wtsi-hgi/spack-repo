# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElrm(RPackage):
	"""Exact Logistic Regression via MCMC

	Implements a Markov Chain Monte Carlo algorithm to approximate 
	exact conditional inference for logistic regression models. Exact 
	conditional inference is based on the distribution of the sufficient 
	statistics for the parameters of interest given the sufficient statistics 
	for the remaining nuisance parameters. Using model formula notation, users 
	specify a logistic model and model terms of interest for exact inference.
	See Zamar et al. (2007) <doi:10.18637/jss.v021.i03> for more details. 
	"""
	
	cran = "elrm" 

	version("1.2.5", md5="2ddcc095ab8f93fc70b222e94d8c5fa8")

	depends_on("r@2.7.2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
