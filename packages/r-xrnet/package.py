# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXrnet(RPackage):
	"""Hierarchical Regularized Regression

	Fits hierarchical regularized regression models
    to incorporate potentially informative external data, Weaver and Lewinger (2019) <doi:10.21105/joss.01761>. 
    Utilizes coordinate descent to efficiently fit regularized regression models both with and without
    external information with the most common penalties used in practice (i.e. ridge, lasso, elastic net). 
    Support for standard R matrices, sparse matrices and big.matrix objects.
	"""
	
	homepage = "https://github.com/USCbiostats/xrnet"
	cran = "xrnet" 

	version("0.1.7", md5="5bae962a6d47b58890b4fedc5cf80c6b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
