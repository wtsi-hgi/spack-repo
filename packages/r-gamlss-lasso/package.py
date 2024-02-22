# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssLasso(RPackage):
	"""Extra Lasso-Type Additive Terms for GAMLSS

	Interface for extra high-dimensional smooth functions for Generalized Additive Models for Location Scale and Shape (GAMLSS) including (adaptive) lasso, ridge, elastic net and least angle regression.
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.lasso" 

	version("1.0-1", md5="41d573c150f71c6633f25c8c694967ee")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gamlss@2.4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
