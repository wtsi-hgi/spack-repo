# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSales(RPackage):
	"""The (Adaptive) Elastic Net and Lasso Penalized Sparse Asymmetric
Least Squares (SALES) and Coupled Sparse Asymmetric Least
Squares (COSALES) using Coordinate Descent and Proximal
Gradient Algorithms

	A coordinate descent algorithm for computing the solution paths of
    the sparse and coupled sparse asymmetric least squares, including the
    (adaptive) elastic net and Lasso penalized SALES and COSALES regressions.
	"""
	
	homepage = "https://github.com/knightgu/SALES"
	cran = "SALES" 

	version("1.0.2", md5="57858ebe9e73d0aaa3812b0b80dc51ce")

	depends_on("r-matrix", type=("build", "run"))
