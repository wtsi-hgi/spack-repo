# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsrglm(RPackage):
	"""Partial Least Squares Regression for Generalized Linear Models

	Provides (weighted) Partial least squares Regression for generalized linear models and repeated k-fold cross-validation of such models using various criteria <arXiv:1810.01005>. It allows for missing data in the explanatory variables. Bootstrap confidence intervals constructions are also available.
	"""
	
	homepage = "https://fbertran.github.io/plsRglm/"
	cran = "plsRglm" 

	version("1.5.1", md5="f79aa542ca1d938c1fe9214e3a298819")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
