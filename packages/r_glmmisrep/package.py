# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmisrep(RPackage):
	"""Generalized Linear Models Adjusting for Misrepresentation

	Fit Generalized Linear Models to continuous and count outcomes, as well as estimate the prevalence of misrepresentation of an important binary predictor. Misrepresentation typically arises when there is an incentive for the binary factor to be misclassified in one direction (e.g., in insurance settings where policy holders may purposely deny a risk status in order to lower the insurance premium). This is accomplished by treating a subset of the response variable as resulting from a mixture distribution. Model parameters are estimated via the Expectation Maximization algorithm and standard errors of the estimates are obtained from closed forms of the Observed Fisher Information. For an introduction to the models and the misrepresentation framework, see Xia et. al., (2023) <https://variancejournal.org/article/73151-maximum-likelihood-approaches-to-misrepresentation-models-in-glm-ratemaking-model-comparisons>.
	"""
	
	cran = "glmMisrep" 

	version("0.1.0", md5="7178de722c4d5ef42a21e551d8b7e27c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-poisson-glm-mix", type=("build", "run"))
