# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadprogxt(RPackage):
	"""Quadratic Programming with Absolute Value Constraints

	Extends the quadprog package to solve quadratic programs with
    absolute value constraints and absolute values in the objective function.
	"""
	
	cran = "quadprogXT" 

	version("0.0.5", md5="5cb416db12a298d3c3b36c289a68e09c")

	depends_on("r-quadprog", type=("build", "run"))
