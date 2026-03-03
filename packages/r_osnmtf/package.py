# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsnmtf(RPackage):
	"""Orthogonal Sparse Non-Negative Matrix Tri-Factorization

	A novel method to implement cancer subtyping and subtype specific drug targets identification via non-negative matrix tri-factorization.
    To improve the interpretability, we introduce orthogonal constraint to the row coefficient matrix and column coefficient matrix. To meet the prior knowledge
    that each subtype should be strongly associated with few gene sets, we introduce sparsity constraint to the association sub-matrix. The average residue was
    introduced to evaluate the row and column cluster numbers. This is part of the work "Liver Cancer Analysis via Orthogonal Sparse Non-Negative Matrix Tri-
    Factorization" which will be submitted to BBRC.
	"""
	
	cran = "OSNMTF" 

	version("0.1.0", md5="bf39abc11a487e3e63bca6e8b8a1fac8")

	depends_on("r@3.4.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
