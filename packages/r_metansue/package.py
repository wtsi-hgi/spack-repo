# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetansue(RPackage):
	"""Meta-Analysis of Studies with Non-Statistically Significant
Unreported Effects

	Novel method to unbiasedly include studies with Non-statistically Significant Unreported Effects (NSUEs) in a meta-analysis. First, the method calculates the interval where the unreported effects (e.g., t-values) should be according to the threshold of statistical significance used in each study. Afterwards, the method uses maximum likelihood techniques to impute the expected effect size of each study with NSUEs, accounting for between-study heterogeneity and potential covariates. Multiple imputations of the NSUEs are then randomly created based on the expected value, variance, and statistical significance bounds. Finally, it conducts a restricted-maximum likelihood random-effects meta-analysis separately for each set of imputations and it conducts estimations from these meta-analyses. Please read the reference in 'metansue' for details of the procedure.
	"""
	
	cran = "metansue" 

	version("2.5", md5="8a50b8e2171409970dc0b5e2508dacbc")

