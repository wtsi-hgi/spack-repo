# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultLatentReg(RPackage):
	"""Regression and Clustering in Multivariate Response Scenarios

	Fitting multivariate response models with random effects on one or two levels; whereby the (one-dimensional) random effect represents a latent variable approximating the multivariate space of outcomes, after possible adjustment for covariates. The method is particularly useful for multivariate, highly correlated outcome variables with unobserved heterogeneities. Applications include regression with multivariate responses, as well as multivariate clustering or ranking problems. See Zhang and Einbeck (2024) <doi:10.1007/s42519-023-00357-0>.
	"""
	
	cran = "mult.latent.reg" 

	version("0.1.6", md5="9d9bb4fc651840cc9bc6c7fa53cdf995")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
