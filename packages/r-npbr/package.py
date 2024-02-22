# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpbr(RPackage):
	"""Nonparametric Boundary Regression

	A variety of functions for the best known and most innovative approaches to nonparametric boundary estimation. The selected methods are concerned with empirical, smoothed, unrestricted as well as constrained fits under both separate and multiple shape constraints. They cover robust approaches to outliers  as well as data envelopment techniques based on piecewise polynomials, splines, local linear fitting, extreme values and kernel smoothing. The package also seamlessly allows for Monte Carlo comparisons among these different estimation methods.  Its use is illustrated via a number of empirical applications and simulated examples.
	"""
	
	cran = "npbr" 

	version("1.8", md5="4217b6e0600ba49abddb3d9df9fa87f9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-benchmarking", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rglpk@0.6.2:", type=("build", "run"))
