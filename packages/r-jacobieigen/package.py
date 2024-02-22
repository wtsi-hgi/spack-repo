# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJacobieigen(RPackage):
	"""Classical Jacobi Eigenvalue Algorithm

	Implements the classical Jacobi algorithm for the
    eigenvalues and eigenvectors of a real symmetric matrix, both in 
    pure 'R' and in 'C++' using 'Rcpp'. Mainly as a programming example 
    for teaching purposes.
	"""
	
	cran = "JacobiEigen" 

	version("0.3-4", md5="655570c5399f68aaaebe380228de6349")

	depends_on("r-rcpp", type=("build", "run"))
