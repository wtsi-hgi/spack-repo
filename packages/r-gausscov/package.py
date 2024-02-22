# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGausscov(RPackage):
	"""The Gaussian Covariate Method for Variable Selection

	Given the standard linear model the traditional way of deciding whether to include the jth covariate is to apply the F-test to decide whether the corresponding beta coefficient is  zero. The Gaussian covariate method is completely different. The question as to whether the beta coefficient is or is not zero is replaced by the question as to whether the covariate is better or worse than i.i.d. Gaussian noise. The P-value for the covariate is the probability that Gaussian noise is better. Surprisingly this can be given exactly and it is the same a the P-value for the classical model based on the F-distribution. The Gaussian covariate P-value is model free, it is the same for any data set. Using the idea it is possible to do covariate selection for a small number of covariates 25 by considering all subsets.  Post selection inference causes no problems as the P-values hold whatever the data. The idea extends to stepwise regression again with exact probabilities. In the simplest version the only parameter is a specified cut-off P-value which can be interpreted as the probability of a false positive being included in the final selection. For more information see the web site below and the accompanying papers: L. Davies and L. Duembgen, "Covariate Selection Based on a Model-free Approach to Linear Regression with Exact Probabilities", 2022, <arxiv:2202.01553>. L. Davies, "Linear Regression, Covariate Selection and the Failure of Modelling", 2022, <arXiv:2112.08738>.
	"""
	
	cran = "gausscov" 

	version("1.0.3", md5="c6cabea16a8f1327b66e793bd35346a4")

	depends_on("r@3.5:", type=("build", "run"))
