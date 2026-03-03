# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsegl(RPackage):
	"""Sparse Group Lasso

	Efficient implementation of sparse group lasso with optional
    bound constraints on the coefficients. It supports the use of a sparse
    design matrix as well as returning coefficient estimates in a sparse
    matrix. Furthermore, it correctly calculates the degrees of freedom to
    allow for information criteria rather than cross-validation with very
    large data. Finally, the interface to compiled code avoids unnecessary
    copies and allows for the use of long integers.
	"""
	
	homepage = "https://github.com/dajmcdon/sparsegl/"
	cran = "sparsegl" 

	version("1.0.2", md5="59218f90c31c3671191b6c34f93df952")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dotcall64", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
