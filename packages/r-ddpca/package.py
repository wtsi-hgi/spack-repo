# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdpca(RPackage):
	"""Diagonally Dominant Principal Component Analysis

	Efficient procedures for fitting the DD-PCA (Ke et al., 2019, <arXiv:1906.00051>)  by decomposing a large covariance matrix into a low-rank matrix plus a diagonally dominant matrix. The implementation of DD-PCA includes the convex approach using the Alternating Direction Method of Multipliers (ADMM) and the non-convex approach using the iterative projection algorithm. Applications of DD-PCA to large covariance matrix estimation and global multiple testing are also included in this package. 
	"""
	
	cran = "ddpca" 

	version("1.1", md5="aa87c12f17b99cce20cd9ee1a4d9c0f0")

	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
