# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmep(RPackage):
	"""Generalized Linear Mixed Model Analysis via Expectation
Propagation

	Approximate frequentist inference for generalized linear mixed model analysis with expectation propagation used to circumvent the need for multivariate integration. In this version, the random effects can be any reasonable dimension. However, only probit mixed models with one level of nesting are supported. The methodology is described in Hall, Johnstone, Ormerod, Wand and Yu (2018) <arXiv:1805.08423v1>.
	"""
	
	cran = "glmmEP" 

	version("1.0-3.1", md5="5413a08aea90bc92bc0fde4a6d71a4e5")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
