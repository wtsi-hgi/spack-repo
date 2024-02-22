# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlinsolve(RPackage):
	"""Iterative Solvers for (Sparse) Linear System of Equations

	Solving a system of linear equations is one of the most fundamental
    computational problems for many fields of mathematical studies, such as
    regression problems from statistics or numerical partial differential equations.
    We provide basic stationary iterative solvers such as Jacobi, Gauss-Seidel,
    Successive Over-Relaxation and SSOR methods. Nonstationary, also known as
	Krylov subspace methods are also provided. Sparse matrix computation is also supported
    in that solving large and sparse linear systems can be manageable using 'Matrix' package
    along with 'RcppArmadillo'. For a more detailed description, see a book by Saad (2003)
    <doi:10.1137/1.9780898718003>.
	"""
	
	cran = "Rlinsolve" 

	version("0.3.2", md5="e46d51438042f92a16e55783544908f3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
