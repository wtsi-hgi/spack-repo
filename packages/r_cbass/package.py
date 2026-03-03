# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbass(RPackage):
	"""Classification -- Bayesian Adaptive Smoothing Splines

	Fit multiclass Classification version of Bayesian Adaptive Smoothing Splines (CBASS) to data using reversible jump MCMC. The multiclass classification problem consists of a response variable that takes on unordered categorical values with at least three levels, and a set of inputs for each response variable. The CBASS model consists of a latent multivariate probit formulation, and the means of the latent Gaussian random variables are specified using adaptive regression splines. The MCMC alternates updates of the latent Gaussian variables and the spline parameters. All the spline parameters (variables, signs, knots, number of interactions), including the number of basis functions used to model each latent mean, are inferred. Functions are provided to process inputs, initialize the chain, run the chain, and make predictions. Predictions are made on a probabilistic basis, where, for a given input, the probabilities of each categorical value are produced. See Marrs and Francom (2023) "Multiclass classification using Bayesian multivariate adaptive regression splines" Under review.
	"""
	
	cran = "cbass" 

	version("0.1", md5="96a4c81d3879ecb812bd3659903153a0")

