# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplines2(RPackage):
	"""Regression Spline Functions and Classes

	Constructs basis functions of B-splines, M-splines,
    I-splines, convex splines (C-splines), periodic splines,
    natural cubic splines, generalized Bernstein polynomials,
    their derivatives, and integrals (except C-splines)
    by closed-form recursive formulas.
    It also contains a C++ head-only library integrated with Rcpp.
    See Wang and Yan (2021) <doi:10.6339/21-JDS1020> for details.
	"""
	
	homepage = "https://wwenjie.org/splines2"
	cran = "splines2" 

	version("0.5.1", md5="a0ca2a9a249064438d912995bc15b5c1", url="https://cran.r-project.org/src/contrib/splines2_0.5.1.tar.gz")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
