# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPldamixture(RPackage):
	"""Post-Linkage Data Analysis Based on Mixture Modelling

	Perform inference in the secondary analysis setting with linked data potentially containing mismatch errors. Only the linked data file may be accessible and information about the record linkage process may be limited or unavailable. Implements the 'General Framework for Regression with Mismatched Data' developed by Slawski et al. (2023) <arXiv:2306.00909>. The framework uses a mixture model for pairs of linked records whose two components reflect distributions conditional on match status, i.e., correct match or mismatch. Inference is based on composite likelihood and the Expectation-Maximization (EM) algorithm. The package currently supports Cox Proportional Hazards Regression (right-censored data only) and Generalized Linear Regression Models (Gaussian, Gamma, Poisson, and Logistic (binary models only)). Information about the underlying record linkage process can be incorporated into the method if available (e.g., assumed overall mismatch rate, safe matches, predictors of match status, or predicted probabilities of correct matches).
	"""
	
	homepage = "https://github.com/bpriy/pldamixture"
	cran = "pldamixture" 

	version("0.1.0", md5="c236f5f3a123e21c86aaf46603544e8b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
