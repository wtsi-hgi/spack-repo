# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBspline(RPackage):
	"""B-Spline Interpolation and Regression

	Build and use B-splines for interpolation and regression.
  In case of regression, equality constraints as well as monotonicity
  and/or positivity of B-spline weights can be imposed. Moreover, 
  knot positions (not only spline weights) can be part of 
  optimized parameters too. For this end, 'bspline' is able to calculate
  Jacobian of basis vectors as function of knot positions. User is provided with 
  functions calculating spline values at arbitrary points. These 
  functions can be differentiated and integrated to obtain B-splines calculating 
  derivatives/integrals at any point. B-splines of this package can 
  simultaneously operate on a series of curves sharing the same set of 
  knots. 'bspline' is written with concern about computing 
  performance that's why the basis and Jacobian calculation is implemented in C++.
  The rest is implemented in R but without notable impact on computing speed.
	"""
	
	homepage = "https://github.com/MathsCell/bspline"
	cran = "bspline" 

	version("2.2", md5="5636735e07c53b7581e0a0c2b087330e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nlsic@1.0.2:", type=("build", "run"))
	depends_on("r-arrapply", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
