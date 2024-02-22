# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQz(RPackage):
	"""Generalized Eigenvalues and QZ Decomposition

	Generalized eigenvalues and eigenvectors
        use QZ decomposition (generalized Schur decomposition).
        The decomposition needs an N-by-N non-symmetric
        matrix A or paired matrices (A,B) with eigenvalues reordering
        mechanism. The decomposition functions are mainly based Fortran
        subroutines in complex*16 and double precision of LAPACK
        library (version 3.10.0 or later).
	"""
	
	cran = "QZ" 

	version("0.2-3", md5="54afc9c6c7cc22c4651884c4de3b783b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
