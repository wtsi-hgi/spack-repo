# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnma(RPackage):
	"""Bayesian Network Meta-Analysis using 'JAGS'

	Network meta-analyses using Bayesian framework following Dias et al. (2013) <DOI:10.1177/0272989X12458724>. Based on the data input, creates prior, model file, and initial values needed to run models in 'rjags'. Able to handle binomial, normal and multinomial arm-level data. Can handle multi-arm trials and includes methods to incorporate covariate and baseline risk effects. Includes standard diagnostics and visualization tools to evaluate the results.
	"""
	
	cran = "bnma" 

	version("1.6.0", md5="e36b912178b8cd5cd8f95006c9e7bee5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
