# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalculus(RPackage):
	"""High Dimensional Numerical and Symbolic Calculus

	Efficient C++ optimized functions for numerical and symbolic calculus as described in Guidotti (2022) <doi:10.18637/jss.v104.i05>. It includes basic arithmetic, tensor calculus, Einstein summing convention, fast computation of the Levi-Civita symbol and generalized Kronecker delta, Taylor series expansion, multivariate Hermite polynomials, high-order derivatives, ordinary differential equations, differential operators (Gradient, Jacobian, Hessian, Divergence, Curl, Laplacian) and numerical integration in arbitrary orthogonal coordinate systems: cartesian, polar, spherical, cylindrical, parabolic or user defined by custom scale factors. 
	"""
	
	homepage = "https://calculus.eguidotti.com"
	cran = "calculus" 

	version("1.0.1", md5="f6dfd47e7f6b5bb3eb611f7390270710")

	depends_on("r-rcpp", type=("build", "run"))
