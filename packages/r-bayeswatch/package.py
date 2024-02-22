# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayeswatch(RPackage):
	"""Bayesian Change-Point Detection for Process Monitoring with
Fault Detection

	Bayes Watch fits an array of Gaussian Graphical Mixture Models to groupings of homogeneous data in time, called regimes, which are modeled as the observed states of a Markov process with unknown transition probabilities.  In doing so, Bayes Watch defines a posterior distribution on a vector of regime assignments, which gives meaningful expressions on the probability of every possible change-point.  Bayes Watch also allows for an effective and efficient fault detection system that assesses what features in the data where the most responsible for a given change-point.  For further details, see: Alexander C. Murph et al. (2023) <arXiv:2310.02940>.
	"""
	
	cran = "bayesWatch" 

	version("0.1.3", md5="7122cbbd28117901a5b1131af5e6c736")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-hotelling", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra@0.9.1:", type=("build", "run"))
	depends_on("r-bdgraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ess", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
