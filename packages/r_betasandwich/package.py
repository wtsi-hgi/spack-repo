# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetasandwich(RPackage):
	"""Robust Confidence Intervals for Standardized Regression
Coefficients

	Generates robust confidence intervals for standardized regression coefficients
    using heteroskedasticity-consistent standard errors for models fitted by lm()
    as described in Dudgeon (2017) <doi:10.1007/s11336-017-9563-z>.
    A description of the package and code examples
    are presented in Pesigan, Sun, and Cheung (2023) <doi:10.1080/00273171.2023.2201277>.
	"""
	
	homepage = "https://github.com/jeksterslab/betaSandwich"
	cran = "betaSandwich" 

	version("1.0.6", md5="20717eeba957e91668e520a259a327e3")

	depends_on("r@3.5:", type=("build", "run"))
