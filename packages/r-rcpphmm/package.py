# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpphmm(RPackage):
	"""Rcpp Hidden Markov Model

	Collection of functions to evaluate sequences, decode hidden states and estimate parameters from a single or multiple sequences of a discrete time Hidden Markov Model. The observed values can be modeled by a multinomial distribution for categorical/labeled emissions, a mixture of Gaussians for continuous data and also a mixture of Poissons for discrete values. It includes functions for random initialization, simulation, backward or forward sequence evaluation, Viterbi or forward-backward decoding and parameter estimation using an Expectation-Maximization approach.
	"""
	
	cran = "RcppHMM" 

	version("1.2.2", md5="b28524c50823cc46136959cba656bbbe")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
