# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesnsgp(RPackage):
	"""Bayesian Analysis of Non-Stationary Gaussian Process Models

	Enables off-the-shelf functionality for fully Bayesian, nonstationary Gaussian process modeling. The approach to nonstationary modeling involves a closed-form, convolution-based covariance function with spatially-varying parameters; these parameter processes can be specified either deterministically (using covariates or basis functions) or stochastically (using approximate Gaussian processes). Stationary Gaussian processes are a special case of our methodology, and we furthermore implement approximate Gaussian process inference to account for very large spatial data sets (Finley, et al (2017) <arXiv:1702.00434v2>). Bayesian inference is carried out using Markov chain Monte Carlo methods via the 'nimble' package, and posterior prediction for the Gaussian process at unobserved locations is provided as a post-processing step.
	"""
	
	cran = "BayesNSGP" 

	version("0.1.2", md5="f9a1e3d28cb04b45edb8ab2c85986c53")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-nimble", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-statmatch", type=("build", "run"))
