# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesbekk(RPackage):
	"""Bayesian Estimation of Bivariate Volatility Model

	The Multivariate Generalized Autoregressive Conditional Heteroskedasticity (MGARCH) models are used for modelling the volatile multivariate data sets. In this package a variant of MGARCH called BEKK (Baba, Engle, Kraft, Kroner) proposed by Engle and Kroner (1995) <http://www.jstor.org/stable/3532933> has been used to estimate the bivariate time series data using Bayesian technique.
	"""
	
	cran = "BayesBEKK" 

	version("0.1.1", md5="542e549a475525a39487c4c22c5d51db")

	depends_on("r-mts", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
