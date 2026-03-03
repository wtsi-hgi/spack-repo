# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvarsv(RPackage):
	"""Bayesian Analysis of a Vector Autoregressive Model with
Stochastic Volatility and Time-Varying Parameters

	R/C++ implementation of the model proposed by Primiceri ("Time Varying Structural Vector Autoregressions and Monetary Policy", Review of Economic Studies, 2005), with functionality for computing posterior predictive distributions and impulse responses.
	"""
	
	homepage = "https://sites.google.com/site/fk83research/code"
	cran = "bvarsv" 

	version("1.1", md5="81d57b5ea3abcd7e42e7811680de782c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
