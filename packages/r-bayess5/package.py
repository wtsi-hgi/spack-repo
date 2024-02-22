# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayess5(RPackage):
	"""Bayesian Variable Selection Using Simplified Shotgun Stochastic
Search with Screening (S5)

	In p >> n settings, full posterior sampling using existing Markov chain Monte
    Carlo (MCMC) algorithms is highly inefficient and often not feasible from a practical
    perspective. To overcome this problem, we propose a scalable stochastic search algorithm that is called the Simplified Shotgun Stochastic Search (S5) and aimed at rapidly explore interesting regions of model space and finding the maximum a posteriori(MAP) model. Also, the S5 provides an approximation of posterior probability of each model (including the marginal inclusion probabilities). This algorithm is a part of an article titled "Scalable Bayesian Variable Selection Using Nonlocal Prior Densities in Ultrahigh-dimensional Settings" (2018) by Minsuk Shin, Anirban Bhattacharya, and Valen E. Johnson and "Nonlocal Functional Priors for Nonparametric Hypothesis Testing and High-dimensional Model Selection" (2020+) by Minsuk Shin and Anirban Bhattacharya. 
	"""
	
	homepage = "https://arxiv.org/abs/1507.07106v4"
	cran = "BayesS5" 

	version("1.41", md5="0fe2e45777c1d577ece150e8e3fb8f91", url="https://cran.r-project.org/src/contrib/BayesS5_1.41.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
