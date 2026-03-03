# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphastable(RPackage):
	"""Inference for Stable Distribution

	Developed to perform the tasks given by the following. 1-computing the probability density function and distribution function of a univariate stable distribution; 2- generating from univariate stable, truncated stable, multivariate elliptically contoured stable, and bivariate strictly stable distributions; 3- estimating the parameters of univariate symmetric stable, skew stable, Cauchy, multivariate elliptically contoured stable, and multivariate strictly stable distributions; 4- estimating
             the parameters of the mixture of symmetric stable and mixture of Cauchy distributions.
	"""
	
	cran = "alphastable" 

	version("0.2.1", md5="efff30b2d741be1fd10f8fdb9973b3c5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
