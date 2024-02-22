# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptisolve(RPackage):
	"""Linear, Quadratic, and Rational Optimization

	Solver for linear, quadratic, and rational programs with linear, quadratic, and rational constraints. A unified interface to different R packages is provided. Optimization problems are transformed into equivalent formulations and solved by the respective package. For example, quadratic programming problems with linear, quadratic and rational constraints can be solved by augmented Lagrangian minimization using package 'alabama', or by sequential quadratic programming using solver 'slsqp'.  Alternatively, they can be reformulated as optimization problems with second order cone constraints and solved with package 'cccp'.
	"""
	
	cran = "optiSolve" 

	version("1.0", md5="956262b807a3b2200d4f95866ee2dd66")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-shapes", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-cccp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpp@0.12.4:", type=("build", "run"))
