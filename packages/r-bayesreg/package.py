# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesreg(RPackage):
	"""Bayesian Regression Models with Global-Local Shrinkage Priors

	Fits linear or generalized linear regression models using Bayesian global-local shrinkage prior hierarchies as described in Polson and Scott (2010) <doi:10.1093/acprof:oso/9780199694587.003.0017>. Provides an efficient implementation of ridge, lasso, horseshoe and horseshoe+ regression with logistic, Gaussian, Laplace, Student-t, Poisson or geometric distributed targets using the algorithms summarized in Makalic and Schmidt (2016) <arXiv:1611.06649>.
	"""
	
	cran = "bayesreg" 

	version("1.2", md5="7cfe2a72ba5b6df5d0c6ec167cac7895")

	depends_on("r-pgdraw@1:", type=("build", "run"))
