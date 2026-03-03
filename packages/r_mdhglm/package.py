# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdhglm(RPackage):
	"""Multivariate Double Hierarchical Generalized Linear Models

	Allows various models for multivariate response variables where each response is assumed to follow double hierarchical generalized linear models. In double hierarchical generalized linear models, the mean, dispersion parameters for variance of random effects, and residual variance can be further modeled as random-effect models.
	"""
	
	cran = "mdhglm" 

	version("1.8", md5="3f2584fe0e7842528ef6b88221adc1c2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
