# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeeverse(RPackage):
	"""A Comprehensive Analysis of High Dimensional Longitudinal Data

	To provide a comprehensive analysis of high dimensional longitudinal
    data,this package provides analysis for any combination of 1) simultaneous
    variable selection and estimation, 2) mean regression or quantile regression
    for heterogeneous data, 3) cross-sectional or longitudinal data, 4) balanced
    or imbalanced data, 5) moderate, high or even ultra-high dimensional data,
    via computationally efficient implementations of penalized generalized
    estimating equations.
	"""
	
	cran = "geeVerse" 

	version("0.1.0", md5="1381a5bf3fb756bf758a115b4a945cf2")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
