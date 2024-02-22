# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparseeigen(RPackage):
	"""Computation of Sparse Eigenvectors of a Matrix

	Computation of sparse eigenvectors of a matrix (aka sparse PCA)
    with running time 2-3 orders of magnitude lower than existing methods and
    better final performance in terms of recovery of sparsity pattern and 
    estimation of numerical values. Can handle covariance matrices as well as 
    data matrices with real or complex-valued entries. Different levels of 
    sparsity can be specified for each individual ordered eigenvector and the 
    method is robust in parameter selection. See vignette for a detailed 
    documentation and comparison, with several illustrative examples. 
    The package is based on the paper:
    K. Benidis, Y. Sun, P. Babu, and D. P. Palomar (2016). "Orthogonal Sparse PCA 
    and Covariance Estimation via Procrustes Reformulation," IEEE Transactions on 
    Signal Processing <doi:10.1109/TSP.2016.2605073>.
	"""
	
	homepage = "https://github.com/dppalomar/sparseEigen"
	cran = "sparseEigen" 

	version("0.1.0", md5="0aea13d5915e16c9cac4adba9e7fe82e")

	depends_on("r@3.4:", type=("build", "run"))
