# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlsic(RPackage):
	"""Non Linear Least Squares with Inequality Constraints

	We solve non linear least squares problems with optional
    equality and/or inequality constraints. Non linear iterations are
    globalized with back-tracking method. Linear problems are solved by
    dense QR decomposition from 'LAPACK' which can limit the size of
    treated problems. On the other side, we avoid condition number
    degradation which happens in classical quadratic programming approach.
    Inequality constraints treatment on each non
    linear iteration is based on 'NNLS' method (by Lawson and Hanson).
    We provide an original function 'lsi_ln' for solving linear least squares
    problem with inequality constraints in least norm sens. Thus if Jacobian of
    the problem is rank deficient a solution still can be provided.
    However, truncation errors are probable in this case.
    Equality constraints are treated by using a basis of Null-space.
    User defined function calculating residuals must return a list having
    residual vector (not their squared sum) and Jacobian. If Jacobian is
    not in the returned list, package 'numDeriv' is used to calculated
    finite difference version of Jacobian. The 'NLSIC' method was fist
    published in Sokol et al. (2012) <doi:10.1093/bioinformatics/btr716>.
	"""
	
	homepage = "https://github.com/MathsCell/nlsic"
	cran = "nlsic" 

	version("1.0.4", md5="40785f5c4f13d3fcbb548eec2fe4b0ef")

	depends_on("r-nnls", type=("build", "run"))
