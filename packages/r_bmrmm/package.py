# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmrmm(RPackage):
	"""An Implementation of the Bayesian Markov (Renewal) Mixed Models

	The Bayesian Markov renewal mixed models take sequentially observed categorical data with continuous duration times, being either state duration or inter-state duration. These models comprehensively analyze the stochastic dynamics of both state transitions and duration times under the influence of multiple exogenous factors and random individual effect. The default setting flexibly models the transition probabilities using Dirichlet mixtures and the duration times using gamma mixtures. It also provides the flexibility of modeling the categorical sequences using Bayesian Markov mixed models alone, either ignoring the duration times altogether or dividing duration time into multiples of an additional category in the sequence by a user-specific unit. The package allows extensive inference of the state transition probabilities and the duration times as well as relevant plots and graphs. It also includes a synthetic data set to demonstrate the desired format of input data set and the utility of various functions. Methods for Bayesian Markov renewal mixed models are as described in: Abhra Sarkar et al., (2018) <doi:10.1080/01621459.2018.1423986> and Yutong Wu et al., (2022) <doi:10.1093/biostatistics/kxac050>.
	"""
	
	cran = "BMRMM" 

	version("1.0.0", md5="f400b8dcc46c3bd853038499413f64f1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-logofgamma", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-multicool", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
