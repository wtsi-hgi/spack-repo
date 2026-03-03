# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetabayes(RPackage):
	"""Bayesian Beta Regression

	Provides a class of Bayesian beta regression models for the analysis of continuous data with support restricted to an unknown finite support. The response variable is modeled using a four-parameter beta distribution with the mean or mode parameter depending linearly on covariates through a link function. When the response support is known to be (0,1), the above class of models reduce to traditional (0,1) supported beta regression models. Model choice is carried out via the logarithm of the pseudo marginal likelihood (LPML), the deviance information criterion (DIC), and the Watanabe-Akaike information criterion (WAIC). See Zhou and Huang (2022) <doi:10.1016/j.csda.2021.107345>.
	"""
	
	cran = "betaBayes" 

	version("1.0.1", md5="5eb186e2b334e8d9238c10a01abd1574")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4.300:", type=("build", "run"))
