# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpandfunctions(RPackage):
	"""Feature Matrix Builder

	Generates feature matrix outputs from R object inputs
    using a variety of expansion functions.  The generated
    feature matrices have applications as inputs
    for a variety of machine learning algorithms.
    The expansion functions are based on coercing the input
    to a matrix, treating the columns as features and
    converting individual columns or combinations into blocks of
    columns.
    Currently these include expansion of columns by
    efficient sparse embedding by vectors of lags,
    quadratic expansion into squares and unique products,
    powers by vectors of degree,
    vectors of orthogonal polynomials functions,
    and block random affine projection transformations (RAPTs).
    The transformations are
    magrittr- and cbind-friendly, and can be used in a
    building block fashion.  For instance, taking the cos() of
    the output of the RAPT transformation generates a
    stationary kernel expansion via Bochner's theorem, and this
    expansion can then be cbind-ed with other features.
    Additionally, there are utilities for replacing features,
    removing rows with NAs,
    creating matrix samples of a given distribution,
    a simple wrapper for LASSO with CV,
    a Freeman-Tukey transform,
    generalizations of the outer function,
    matrix size-preserving discrete difference by row,
    plotting, etc.
	"""
	
	cran = "expandFunctions" 

	version("0.1.0", md5="5b71b4bfc3a2f7f4bb673eb3c21331b0")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
