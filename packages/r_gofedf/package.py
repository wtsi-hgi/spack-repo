# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofedf(RPackage):
	"""Goodness of Fit Tests Based on Empirical Distribution Functions

	Routines that allow the user to run goodness of fit tests based on empirical distribution functions for formal model evaluation in a general likelihood model. In addition, functions are provided to test a sample against Normal or Gamma distributions, validate the normality assumptions in a linear model, and examine the appropriateness of a Gamma distribution in generalized linear models with various link functions. Michael Arthur Stephens (1976) <http://www.jstor.org/stable/2958206>.
	"""
	
	homepage = "https://github.com/pnickchi/gofedf"
	cran = "gofedf" 

	version("0.1.0", md5="95c6a59d8dd03f552f43499e29aba78a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
