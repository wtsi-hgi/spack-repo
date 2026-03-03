# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemsfa(RPackage):
	"""Semiparametric Estimation of Stochastic Frontier Models

	Semiparametric Estimation of Stochastic Frontier Models following a two step procedure: in the first step semiparametric or nonparametric regression techniques are used to relax parametric restrictions of the functional form representing technology and in the second step variance parameters are obtained by pseudolikelihood estimators or by method of moments.
	"""
	
	cran = "semsfa" 

	version("1.1", md5="192669a68f542b0381a2d9c339902bae")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
