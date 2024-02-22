# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBart(RPackage):
	"""Bayesian Additive Regression Trees

	Bayesian Additive Regression Trees (BART) provide flexible nonparametric modeling of covariates for continuous, binary, categorical and time-to-event outcomes.  For more information see Sparapani, Spanbauer and McCulloch <doi:10.18637/jss.v097.i01>.
	"""
	
	cran = "BART" 

	version("2.9.6", md5="d241e8d6821f7557cf61b35596eea35b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
