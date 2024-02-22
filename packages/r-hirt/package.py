# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHirt(RPackage):
	"""Hierarchical Item Response Theory Models

	Implementation of a class of hierarchical item response
  theory (IRT) models where both the mean and the variance of latent preferences
  (ability parameters) may depend on observed covariates. The current
  implementation includes both the two-parameter latent trait model for binary data and the
  graded response model for ordinal data. Both are fitted via the Expectation-Maximization (EM)
  algorithm. Asymptotic standard errors are derived from the observed information
  matrix.
	"""
	
	homepage = "http://github.com/xiangzhou09/hIRT"
	cran = "hIRT" 

	version("0.3.0", md5="279db19ee4089bc1e24f5f436d0ecd47")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pryr@0.1.2:", type=("build", "run"))
	depends_on("r-rms@5.1.1:", type=("build", "run"))
	depends_on("r-ltm@1.1.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.10:", type=("build", "run"))
