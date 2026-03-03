# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWemix(RPackage):
	"""Weighted Mixed-Effects Models Using Multilevel Pseudo Maximum
Likelihood Estimation

	Run mixed-effects models that include weights at every level. The WeMix package fits a weighted mixed model, also known as a multilevel, mixed, or hierarchical linear model (HLM). The weights could be inverse selection probabilities, such as those developed for an education survey where schools are sampled probabilistically, and then students inside of those schools are sampled probabilistically. Although mixed-effects models are already available in R, WeMix is unique in implementing methods for mixed models using weights at multiple levels. Both linear and logit models are supported. Models may have up to three levels. Random effects are estimated using the PIRLS algorithm from 'lme4pureR' (Walker and Bates (2013) <https://github.com/lme4/lme4pureR>).
	"""
	
	homepage = "https://american-institutes-for-research.github.io/WeMix/"
	cran = "WeMix" 

	version("4.0.3", md5="63fc6a8e3c5f67966128e32cdbb9519c")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix@1.5.4.1:", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
