# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiqp(RPackage):
	"""R Interface to Proximal Interior Point Quadratic Programming
Solver

	An embedded proximal interior point quadratic programming solver, which can solve dense and sparse quadratic programs, described in Schwan, Jiang, Kuhn, and Jones (2023) <doi:10.48550/arXiv.2304.00290>. Combining an infeasible interior point method with the proximal method of multipliers, the algorithm can handle ill-conditioned convex quadratic programming problems without the need for linear independence of the constraints. The solver is written in header only 'C++ 14' leveraging the 'Eigen' library for vectorized linear algebra. For small dense problems, vectorized instructions and cache locality can be exploited more efficiently. Allocation free problem updates and re-solves are also provided.
	"""
	
	homepage = "https://predict-epfl.github.io/piqp-r/"
	cran = "piqp" 

	version("0.2.2", md5="e4ed1eeb4ae3ee902e9cabdfd26cbdde")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
