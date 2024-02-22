# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymbolicdeterminants(RPackage):
	"""Symbolic Representation of Matrix Determinant

	Creates a numeric guide for writing the formula for the determinant of a square matrix (a detguide) as a function of the elements of the matrix and writes out that formula, the symbolic representation.
	"""
	
	cran = "SymbolicDeterminants" 

	version("2.0.0", md5="9f1f32e9d10ec13edb3d7a6a8776979e")

	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
