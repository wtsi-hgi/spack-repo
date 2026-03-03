# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVlmcx(RPackage):
	"""Variable Length Markov Chain with Exogenous Covariates

	Models categorical time series through a Markov Chain when a) covariates are predictors for transitioning into the next state/symbol and b) when the dependence in the past states has variable length. The probability of transitioning to the next state in the Markov Chain is defined by a multinomial regression whose parameters depend on the past states of the chain and, moreover, the number of states in the past needed to predict the next state also depends on the observed states themselves. See Zambom, Kim, and Garcia (2022) <doi:10.1111/jtsa.12615>.
	"""
	
	cran = "VLMCX" 

	version("1.0", md5="b9c7d655b7eb5cd9e361981f10c16acc")

	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
