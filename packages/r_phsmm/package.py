# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhsmm(RPackage):
	"""Penalised Maximum Likelihood Estimation for Hidden Semi-Markov
Models

	Provides tools for penalised maximum likelihood estimation of hidden semi-Markov models (HSMMs) with flexible state dwell-time distributions. These include functions for model fitting, model checking and state-decoding. The package considers HSMMs for univariate time series with state-dependent gamma, normal, Poisson or Bernoulli distributions. For details, see Pohle, J., Adam, T. and Beumer, L.T. (2021): Flexible estimation of the state dwell-time distribution in hidden semi-Markov models. <arXiv:2101.09197>.
	"""
	
	cran = "PHSMM" 

	version("1.0", md5="91994c5e93dd8728f11bce8c71021337")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
