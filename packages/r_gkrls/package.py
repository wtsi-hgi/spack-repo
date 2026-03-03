# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGkrls(RPackage):
	"""Generalized Kernel Regularized Least Squares

	Kernel regularized least squares, also known as kernel ridge regression, 
    is a flexible machine learning method. This package implements this method by 
    providing a smooth term for use with 'mgcv' and uses random sketching to 
    facilitate scalable estimation on large datasets. It provides additional 
    functions for calculating marginal effects after estimation and for use with 
    ensembles ('SuperLearning'), double/debiased machine learning ('DoubleML'), 
    and robust/clustered standard errors ('sandwich'). Chang and Goplerud (2023)
    <arXiv:2209.14355> provide further details.
	"""
	
	homepage = "https://github.com/mgoplerud/gKRLS"
	cran = "gKRLS" 

	version("1.0.2", md5="96a4ad9f6514b0794fe20ef566d5856f")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-sandwich@2.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
