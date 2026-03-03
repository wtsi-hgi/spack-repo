# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimme(RPackage):
	"""Eigenvalues and Singular Values and Vectors from Large Matrices

	
    R interface to 'PRIMME' <https://www.cs.wm.edu/~andreas/software/>, a C library for computing a few
    eigenvalues and their corresponding eigenvectors of a real symmetric or complex
    Hermitian matrix, or generalized Hermitian eigenproblem.  It can also compute
    singular values and vectors of a square or rectangular matrix. 'PRIMME' finds
    largest, smallest, or interior singular/eigenvalues and can use preconditioning
    to accelerate convergence. General description of the methods are provided in the papers
    Stathopoulos (2010, <doi:10.1145/1731022.1731031>) and Wu (2017, <doi:10.1137/16M1082214>).
    See 'citation("PRIMME")' for details.
	"""
	
	homepage = "https://www.cs.wm.edu/~andreas/software/"
	cran = "PRIMME" 

	version("3.2-6", md5="40d882356c99994d559273abf0ce2cf1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
