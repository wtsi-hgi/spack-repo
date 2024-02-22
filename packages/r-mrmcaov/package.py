# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrmcaov(RPackage):
	"""Multi-Reader Multi-Case Analysis of Variance

	Estimation and comparison of the performances of diagnostic tests
    in multi-reader multi-case studies where true case statuses (or ground
    truths) are known and one or more readers provide test ratings for multiple
    cases.  Reader performance metrics are provided for area under and expected
    utility of ROC curves, likelihood ratio of positive or negative tests, and
    sensitivity and specificity.  ROC curves can be estimated empirically or
    with binormal or binormal likelihood-ratio models.  Statistical comparisons
    of diagnostic tests are based on the ANOVA model of Obuchowski-Rockette and
    the unified framework of Hillis (2005) <doi:10.1002/sim.2024>.  The ANOVA
    can be conducted with data from a full factorial, nested, or partially
    paired study design; with random or fixed readers or cases; and covariances
    estimated with the DeLong method, jackknifing, or an unbiased method.  Smith
    and Hillis (2020) <doi:10.1117/12.2549075>.
	"""
	
	homepage = "https://github.com/brian-j-smith/MRMCaov"
	cran = "MRMCaov" 

	version("0.3.0", md5="ce5c1ac235b5033f7becba90d05822b5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
