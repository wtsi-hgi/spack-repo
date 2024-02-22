# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmselect(RPackage):
	"""Bayesian Model Selection for Generalized Linear Mixed Models

	A Bayesian model selection approach for generalized linear mixed models.
    Currently, 'GLMMselect' can be used for Poisson GLMM and Bernoulli GLMM. 'GLMMselect' can select fixed effects and random effects simultaneously. 
    Covariance structures for the random effects are a product of a unknown scalar and a known semi-positive definite matrix.
    'GLMMselect' can be widely used in areas such as longitudinal studies, genome-wide association studies, and spatial statistics.
    'GLMMselect' is based on Xu, Ferreira, Porter, and Franck (202X), Bayesian Model Selection Method for Generalized Linear Mixed Models, Biometrics, under review.
	"""
	
	cran = "GLMMselect" 

	version("1.2.0", md5="36ff65ee5dc0a86123166af342d480b3")

	depends_on("r@3.5:", type=("build", "run"))
