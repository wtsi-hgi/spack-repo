# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpca(RPackage):
	"""RobustPCA: Decompose a Matrix into Low-Rank and Sparse
Components

	Suppose we have a data matrix, which is the superposition of a low-rank component and a sparse component. Candes, E. J., Li, X., Ma, Y., & Wright, J. (2011). Robust principal component analysis?. Journal of the ACM (JACM), 58(3), 11. prove that we can recover each component individually under some suitable assumptions. It is possible to recover both the low-rank and the sparse components exactly by solving a very convenient convex program called Principal Component Pursuit; among all feasible decompositions, simply minimize a weighted combination of the nuclear norm and of the L1 norm. This package implements this decomposition algorithm resulting with Robust PCA approach.
	"""
	
	cran = "rpca" 

	version("0.2.3", md5="c96bf53cac208210b3bb3db2db76949e")

