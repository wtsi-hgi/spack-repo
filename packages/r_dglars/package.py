# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDglars(RPackage):
	"""Differential Geometric Least Angle Regression

	Differential geometric least angle regression method for fitting sparse generalized linear models. In this version of the package, the user can fit models specifying Gaussian, Poisson, Binomial, Gamma and Inverse Gaussian family. Furthermore, several link functions can be used to model the relationship between the conditional expected value of the response variable and the linear predictor. The solution curve can be computed using an efficient predictor-corrector or a cyclic coordinate descent algorithm, as described in the paper linked to via the URL below.
	"""
	
	homepage = "https://www.jstatsoft.org/v59/i08/."
	cran = "dglars" 

	version("2.1.7", md5="90e1e794ea8d6ae6d0647b4da5629093")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
