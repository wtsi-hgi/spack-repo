# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBff(RPackage):
	"""Bayes Factor Functions

	Bayes factors represent the ratio of probabilities assigned to data by competing scientific hypotheses. However, one drawback of Bayes factors is their dependence on prior specifications that define null and alternative hypotheses. Additionally, there are challenges in their computation. To address these issues, we define Bayes factor functions (BFFs) directly from common test statistics. BFFs express Bayes factors as a function of the prior densities used to define the alternative hypotheses. These prior densities are centered on standardized effects, which serve as indices for the BFF. Therefore, BFFs offer a summary of evidence in favor of alternative hypotheses that correspond to a range of scientifically interesting effect sizes. Such summaries remove the need for arbitrary thresholds to determine "statistical significance." BFFs are available in closed form and can be easily computed from z, t, chi-squared, and F statistics. They depend on hyperparameters "r" and "tau^2", which determine the shape and scale of the prior distributions defining the alternative hypotheses. For replicated designs, the "r" parameter in each function can be adjusted to be greater than 1. Plots of BFFs versus effect size provide informative summaries of hypothesis tests that can be easily aggregated across studies.
	"""
	
	cran = "BFF" 

	version("3.0.1", md5="6e6a219c3cf0e7862a8b52a18bdc76f2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bsda", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
