# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJacobi(RPackage):
	"""Jacobi Theta Functions and Related Functions

	Evaluation of the Jacobi theta functions and related
    functions: Weierstrass elliptic function, Weierstrass sigma function,
    Weierstrass zeta function, Klein j-function, Dedekind eta function,
    lambda modular function, Jacobi elliptic functions, Neville theta
    functions, Eisenstein series, lemniscate elliptic functions, elliptic 
    alpha function, Rogers-Ramanujan continued fractions, and Dixon 
    elliptic functions. Complex values of the variable are supported.
	"""
	
	homepage = "https://github.com/stla/jacobi"
	cran = "jacobi" 

	version("3.1.1", md5="45bcd4826fa225483686b3dfbc098a9a")

	depends_on("r-carlson", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
