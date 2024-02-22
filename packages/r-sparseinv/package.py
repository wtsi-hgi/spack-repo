# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparseinv(RPackage):
	"""Computation of the Sparse Inverse Subset

	Creates a wrapper for the 'SuiteSparse' routines 
    that execute the Takahashi equations. These equations compute the
    elements of the inverse of a sparse matrix at locations where the
    its Cholesky factor is structurally non-zero. The resulting matrix is known as a 
	sparse inverse subset. Some helper functions are also implemented. 
	Support for spam matrices is currently limited and will be implemented 
	in the future. See Rue and Martino (2007) <doi:10.1016/j.jspi.2006.07.016> 
	and Zammit-Mangion and Rougier (2018) <doi:10.1016/j.csda.2018.02.001> for the 
	application of these equations to statistics.
	"""
	
	cran = "sparseinv" 

	version("0.1.3", md5="b8685851c3d55026ce7d35866a48a921")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
