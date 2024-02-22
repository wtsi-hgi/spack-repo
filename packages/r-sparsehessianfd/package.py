# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsehessianfd(RPackage):
	"""Numerical Estimation of Sparse Hessians

	Estimates Hessian of a scalar-valued function, and returns it
    in a sparse Matrix format. The sparsity pattern must be known in advance. The
    algorithm is especially efficient for hierarchical models with a large number of
    heterogeneous units.  See Braun, M. (2017) <doi:10.18637/jss.v082.i10>.
	"""
	
	homepage = "https://braunm.github.io/sparseHessianFD/"
	cran = "sparseHessianFD" 

	version("0.3.3.7", md5="8fbe00ab5c974434fa03beef9fbede33")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix@1.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
