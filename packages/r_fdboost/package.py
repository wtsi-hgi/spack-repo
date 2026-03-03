# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdboost(RPackage):
	"""Boosting Functional Regression Models

	Regression models for functional data, i.e., scalar-on-function,
    function-on-scalar and function-on-function regression models, are fitted
    by a component-wise gradient boosting algorithm. 
	For a manual on how to use 'FDboost', see Brockhaus, Ruegamer, Greven (2017) <doi:10.18637/jss.v094.i10>.
	"""
	
	homepage = "https://github.com/boost-R/FDboost"
	cran = "FDboost" 

	version("1.1-2", md5="f1abaf07705028479499b7ff9428c8b4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mboost@2.9.0:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gamboostlss@2.0.0:", type=("build", "run"))
	depends_on("r-stabs", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
