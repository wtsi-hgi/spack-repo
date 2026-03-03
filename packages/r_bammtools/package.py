# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBammtools(RPackage):
	"""Analysis and Visualization of Macroevolutionary Dynamics on
Phylogenetic Trees

	Provides functions for analyzing and visualizing complex
    macroevolutionary dynamics on phylogenetic trees. It is a companion
    package to the command line program BAMM (Bayesian Analysis of
    Macroevolutionary Mixtures) and is entirely oriented towards the analysis,
    interpretation, and visualization of evolutionary rates. Functionality
    includes visualization of rate shifts on phylogenies, estimating
    evolutionary rates through time, comparing posterior distributions of
    evolutionary rates across clades, comparing diversification models using
    Bayes factors, and more.
	"""
	
	homepage = "http://bamm-project.org/"
	cran = "BAMMtools" 

	version("2.1.11", md5="8b872f0a34768a5d7b6528ec09b79bfa")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
