# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetcox(RPackage):
	"""Structural Learning in Cox Models with Time-Dependent Covariates

	Efficient procedures for fitting and cross-validating the overlapping group Lasso (implemented in C++) for Cox models with time-dependent covariates. The penalty term is a weighted sum of infinity norms of (overlapping) groups of coefficients, which can select variables structurally with a specific grouping structure.
	"""
	
	cran = "netcox" 

	version("1.0.1", md5="382d4155cbd78945f329a67e93df6b35")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
