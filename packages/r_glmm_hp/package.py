# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmHp(RPackage):
	"""Hierarchical Partitioning of Marginal R2 for Generalized
Mixed-Effect Models

	Conducts hierarchical partitioning to calculate individual contributions of each predictor (fixed effects) towards marginal R2 for generalized linear mixed-effect model (including lm, glm and glmm) based on output of r.squaredGLMM() in 'MuMIn', applying the algorithm of Lai J.,Zou Y., Zhang S.,Zhang X.,Mao L.(2022)glmm.hp: an R package for computing individual effect of predictors in generalized linear mixed models.Journal of Plant Ecology,15(6)1302-1307<doi:10.1093/jpe/rtac096>.
	"""
	
	homepage = "https://github.com/laijiangshan/glmm.hp"
	cran = "glmm.hp" 

	version("0.1-2", md5="4bfe26492899b6ca4253f9af27d10f59")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
