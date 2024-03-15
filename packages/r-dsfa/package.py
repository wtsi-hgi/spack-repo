# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsfa(RPackage):
	"""Distributional Stochastic Frontier Analysis

	Framework to fit distributional stochastic frontier models. Casts the stochastic frontier model into the flexible framework of distributional regression or otherwise known as General Additive Models of Location, Scale and Shape (GAMLSS). Allows for linear, non-linear, random and spatial effects on all the parameters of the distribution of the output, e.g. effects on the production or cost function, heterogeneity of the noise and inefficiency. Available distributions are the normal-halfnormal and normal-exponential distribution. Estimation via the fast and reliable routines of the 'mgcv' package. For more details see <doi:10.1016/j.csda.2023.107796>.
	"""
	
	cran = "dsfa" 

	version("2.0.2", md5="2a817b3aab60b1e2ae8a0ce1cba64b3d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-gratia", type=("build", "run"))
