# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhs(RPackage):
	"""Graphical Horseshoe MCMC Sampler Using Data Augmented Block
Gibbs Sampler

	Draw posterior samples to estimate the precision matrix for multivariate Gaussian data. Posterior means of the samples is the graphical horseshoe estimate by Li, Bhadra and Craig(2017) <arXiv:1707.06661>. The function uses matrix decomposition and variable change from the Bayesian graphical lasso by Wang(2012) <doi:10.1214/12-BA729>, and the variable augmentation for sampling under the horseshoe prior by Makalic and Schmidt(2016) <arXiv:1508.03884>. Structure of the graphical horseshoe function was inspired by the Bayesian graphical lasso function using blocked sampling, authored by Wang(2012) <doi:10.1214/12-BA729>.
	"""
	
	cran = "GHS" 

	version("0.1", md5="0c0e4d390e5f4b3adef1644ea2eeb9ee")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
