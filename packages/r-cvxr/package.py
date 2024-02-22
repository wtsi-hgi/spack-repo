# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvxr(RPackage):
	"""Disciplined Convex Optimization.

	An object-oriented modeling language for disciplined convex programming
	(DCP) as described in Fu, Narasimhan, and Boyd (2020,
	<doi:10.18637/jss.v094.i14>). It allows the user to formulate convex
	optimization problems in a natural way following mathematical convention
	and DCP rules. The system analyzes the problem, verifies its convexity,
	converts it into a canonical form, and hands it off to an appropriate
	solver to obtain the solution. Interfaces to solvers on CRAN and elsewhere
	are provided, both commercial and open source."""

	cran = "CVXR"

	version("1.0-12", md5="8137d36b071cb966856e093ff18ce7c3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-ecosolver@0.5.4:", type=("build", "run"))
	depends_on("r-scs@3:", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
