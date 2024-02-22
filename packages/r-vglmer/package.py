# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVglmer(RPackage):
	"""Variational Inference for Hierarchical Generalized Linear Models

	Estimates hierarchical models using mean-field variational Bayes. 
    At present, it can estimate logistic, linear, and negative binomial models. 
    It can accommodate models with an arbitrary number of random effects and 
    requires no integration to estimate. It also provides the ability to improve 
    the quality of the approximation using marginal augmentation. 
    Goplerud (2022) <doi:10.1214/21-BA1266> provides details on the variational
    algorithms.
	"""
	
	homepage = "https://github.com/mgoplerud/vglmer"
	cran = "vglmer" 

	version("1.0.3", md5="dca9300b2266e399d15cbbd62dad3433")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
