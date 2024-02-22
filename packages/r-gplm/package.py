# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGplm(RPackage):
	"""Generalized Partial Linear Models (GPLM)

	Provides functions for estimating a generalized partial
	     linear model, a semiparametric variant of the generalized linear model
	     (GLM) which replaces the linear predictor by the sum of a linear
	     and a nonparametric function.
	"""
	
	cran = "gplm" 

	version("0.7-4", md5="d89d6f6d5152d042de367324cf68a41c")

	depends_on("r-aer", type=("build", "run"))
