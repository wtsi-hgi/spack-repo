# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcgee(RPackage):
	"""Bias-Corrected Estimates for Generalized Linear Models for
Dependent Data

	Provides bias-corrected estimates for the regression coefficients of a marginal model estimated with generalized estimating equations. Details about the bias formula used are in Lunardon, N., Scharfstein, D. (2017) <doi:10.1002/sim.7366>.
	"""
	
	cran = "BCgee" 

	version("0.1.1", md5="cf6f60da5edbbee1ca0e1839dce7372f")

	depends_on("r@2.10:", type=("build", "run"))
