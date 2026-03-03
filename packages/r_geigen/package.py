# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeigen(RPackage):
	"""Calculate Generalized Eigenvalues, the Generalized Schur
Decomposition and the Generalized Singular Value Decomposition
of a Matrix Pair with Lapack

	Functions to compute generalized eigenvalues and eigenvectors,
             the generalized Schur decomposition and
             the generalized Singular Value Decomposition of a matrix pair,
             using Lapack routines.
	"""
	
	cran = "geigen" 

	version("2.3", md5="08951fde411893278e127769a9cfa394")

	depends_on("r@3.5:", type=("build", "run"))
