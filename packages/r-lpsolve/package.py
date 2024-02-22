# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpsolve(RPackage):
	"""Interface to 'Lp_solve' v. 5.5 to Solve Linear/Integer Programs.

	Lp_solve is freely available (under LGPL 2) software for solving linear,
	integer and mixed integer programs. In this implementation we supply a
	"wrapper" function in C and some R functions that solve general
	linear/integer problems, assignment problems, and transportation problems.
	This version calls lp_solve"""

	cran = "lpSolve"

	version("5.6.20", md5="82005adb4666e53da367a88885842a17")

