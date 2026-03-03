# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnmatrix(RPackage):
	"""Annotated Matrix: Matrices with Persistent Row and Column
Annotations

	Implements persistent row and column annotations for R matrices. The annotations associated with rows and columns are preserved after subsetting, transposition, and various other matrix-specific operations. Intended use case is for storing and manipulating genomic datasets which typically consist of a matrix of measurements (like gene expression values) as well as annotations about rows (i.e. genomic locations) and annotations about columns (i.e. meta-data about collected samples). But 'annmatrix' objects are also expected to be useful in various other contexts.
	"""
	
	homepage = "https://github.com/karoliskoncevicius/annmatrix"
	cran = "annmatrix" 

	version("0.1.2", md5="83551e9f05a2a47b93214201ee1656a4")

	depends_on("r@4.3:", type=("build", "run"))
