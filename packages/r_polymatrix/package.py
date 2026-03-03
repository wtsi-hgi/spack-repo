# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolymatrix(RPackage):
	"""Infrastructure for Manipulation Polynomial Matrices

	
  Implementation of class "polyMatrix" for storing a matrix of polynomials and implements 
  basic matrix operations; including a determinant and characteristic polynomial.
  It is based on the package 'polynom' and uses a lot of its methods to implement matrix operations.
  This package includes 3 methods of triangularization of polynomial matrices:
  Extended Euclidean algorithm which is most classical but numerically unstable;
  Sylvester algorithm based on LQ decomposition;
  Interpolation algorithm is based on LQ decomposition and Newton interpolation.
  Both methods are described in 
  D. Henrion & M. Sebek, Reliable numerical methods for polynomial matrix triangularization,
  IEEE Transactions on Automatic Control (Volume 44, Issue 3, Mar 1999, Pages 497-508) <doi:10.1109/9.751344>
  and in 
  Salah Labhalla, Henri Lombardi & Roger Marlin, 
  Algorithmes de calcule de la reduction de Hermite d'une matrice a coefficients polynomeaux,
  Theoretical Computer Science (Volume 161, Issue 1-2, July 1996, Pages 69-92) <doi:10.1016/0304-3975(95)00090-9>.
	"""
	
	homepage = "https://github.com/namezys/polymatrix"
	cran = "polyMatrix" 

	version("0.9.16", md5="b692cc339761ca5d8bca393a4cdeb5e4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
