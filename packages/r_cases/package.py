# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCases(RPackage):
	"""Stratified Evaluation of Subgroup Classification Accuracy

	Enables simultaneous statistical inference for the accuracy of multiple classifiers in multiple subgroups (strata). For instance, allows to perform multiple comparisons in diagnostic accuracy studies with co-primary endpoints sensitivity and specificity. (Westphal, Max, and Antonia Zapf. (2021). "Statistical Inference for Diagnostic Test Accuracy Studies with Multiple Comparisons." <arXiv:2105.13469>.)
	"""
	
	homepage = "https://github.com/maxwestphal/cases"
	cran = "cases" 

	version("0.1.1", md5="75f042b681f954f989048167df30cc1b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bindata", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
