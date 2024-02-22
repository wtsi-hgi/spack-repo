# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGplsim(RPackage):
	"""Spline Estimation for GPLSIM

	We provides functions that employ splines to estimate generalized 
             partially linear single index models (GPLSIM), which extend the generalized linear 
             models to include nonlinear effect for some predictors. Please see Y. (2017) at
             <doi:10.1007/s11222-016-9639-0> and Y., and R. (2002) at <doi:10.1198/016214502388618861> for more details.
	"""
	
	cran = "gplsim" 

	version("1.0.0", md5="f86ba6577e0ad180134b453dc64ac3ec")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
