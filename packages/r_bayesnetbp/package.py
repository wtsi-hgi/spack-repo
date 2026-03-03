# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesnetbp(RPackage):
	"""Bayesian Network Belief Propagation

	Belief propagation methods in Bayesian Networks to propagate evidence through the network. The implementation of these methods are based on the article: Cowell, RG (2005). Local Propagation in Conditional Gaussian Bayesian Networks <https://www.jmlr.org/papers/v6/cowell05a.html>. For details please see Yu et. al. (2020) BayesNetBP: An R Package for Probabilistic Reasoning in Bayesian Networks <doi:10.18637/jss.v094.i03>. The optional 'cyjShiny' package for running the Shiny app is available at <https://github.com/cytoscape/cyjShiny>. Please see the example in the documentation of 'runBayesNetApp' function for installing 'cyjShiny' package from GitHub. 
	"""
	
	cran = "BayesNetBP" 

	version("1.6.1", md5="8148dbd5abf2bd86e7c26f4c80faf3bc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
