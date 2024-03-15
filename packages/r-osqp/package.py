# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsqp(RPackage):
	"""Quadratic Programming Solver using the 'OSQP' Library.

	Provides bindings to the 'OSQP' solver. The 'OSQP' solver is a numerical
	optimization package or solving convex quadratic programs written in 'C'
	and based on the alternating direction method of multipliers. See
	<arXiv:1711.08013> for details."""

	cran = "osqp"

	license("Apache-2.0 OR custom")

	version("0.6.3.2", md5="d6b45409799ce483514cada5818fa47a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.6.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
