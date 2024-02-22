# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmn(RPackage):
	"""Inference for Linear Models with Nuisance Parameters

	Efficient Frequentist profiling and Bayesian marginalization of parameters for which the conditional likelihood is that of a multivariate linear regression model.  Arbitrary inter-observation error correlations are supported, with optimized calculations provided for independent-heteroskedastic and stationary dependence structures.
	"""
	
	homepage = "https://github.com/mlysy/LMN"
	cran = "LMN" 

	version("1.1.3", md5="12b2b6cbab7b0bfa03fa09854cc9e817")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-supergauss", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
