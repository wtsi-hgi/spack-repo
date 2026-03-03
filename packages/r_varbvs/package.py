# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarbvs(RPackage):
	"""Large-Scale Bayesian Variable Selection Using Variational
Methods

	Fast algorithms for fitting Bayesian variable selection
    models and computing Bayes factors, in which the outcome (or
    response variable) is modeled using a linear regression or a
    logistic regression. The algorithms are based on the variational
    approximations described in "Scalable variational inference for
    Bayesian variable selection in regression, and its accuracy in
    genetic association studies" (P. Carbonetto & M. Stephens, 2012,
    <DOI:10.1214/12-BA703>). This software has been applied to large
    data sets with over a million variables and thousands of samples.
	"""
	
	homepage = "https://github.com/pcarbo/varbvs"
	cran = "varbvs" 

	version("2.6-10", md5="4784b44a21e44c12d9ca1cd968678a99")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
