# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmPredict(RPackage):
	"""Predicted Values and Discrete Changes for Regression Models

	Functions to calculate predicted values and the difference between
    the two cases with confidence interval for lm() [linear model], glm() [generalized linear model], glm.nb() [negative binomial model],
	polr() [ordinal logistic model], vglm() [generalized ordinal logistic model],	multinom() [multinomial model], tobit() [tobit model],
	svyglm() [survey-weighted generalised linear models] and lmer() [linear multilevel models] using Monte Carlo simulations or bootstrap. Reference: Bennet A. Zelner (2009) <doi:10.1002/smj.783>.
	"""
	
	homepage = "https://github.com/benjaminschlegel/glm.predict/"
	cran = "glm.predict" 

	version("4.3-0", md5="03e8dccfd02a9985e8b6aab109ac8858")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
