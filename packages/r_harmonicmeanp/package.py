# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmonicmeanp(RPackage):
	"""Harmonic Mean p-Values and Model Averaging by Mean Maximum
Likelihood

	The harmonic mean p-value (HMP) test combines p-values and corrects for multiple testing while controlling the strong-sense family-wise error rate. It is more powerful than common alternatives including Bonferroni and Simes procedures when combining large proportions of all the p-values, at the cost of slightly lower power when combining small proportions of all the p-values. It is more stringent than controlling the false discovery rate, and possesses theoretical robustness to positive correlations between tests and unequal weights. It is a multi-level test in the sense that a superset of one or more significant tests is certain to be significant and conversely when the superset is non-significant, the constituent tests are certain to be non-significant. It is based on MAMML (model averaging by mean maximum likelihood), a frequentist analogue to Bayesian model averaging, and is theoretically grounded in generalized central limit theorem. For detailed examples type vignette("harmonicmeanp") after installation. Version 3.0 addresses errors in versions 1.0 and 2.0 that led function p.hmp to control the familywise error rate only in the weak sense, rather than the strong sense as intended.
	"""
	
	cran = "harmonicmeanp" 

	version("3.0.1", md5="04b40580684b0c072b43387b1c98518e")

	depends_on("r-fmstable", type=("build", "run"))
