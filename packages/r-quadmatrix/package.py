# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadmatrix(RPackage):
	"""Solving Quadratic Matrix Equations

	Given inputs A,B and C, this package solves the matrix equation A*X^2 - B*X - C = 0.
	"""
	
	cran = "quadmatrix" 

	version("0.1.0", md5="0631d7b26ab7d44cd00f524f135bc8e8")

	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
