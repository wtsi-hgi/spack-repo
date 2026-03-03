# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBestridge(RPackage):
	"""A Comprehensive R Package for Best Subset Selection

	The bestridge package is designed to provide a one-stand service for users to successfully carry out best ridge regression in various complex situations via the primal dual active set algorithm proposed by Wen, C., Zhang, A., Quan, S. and Wang, X. (2020) <doi:10.18637/jss.v094.i04>. This package allows users to perform the regression, classification, count regression and censored regression for (ultra) high dimensional data, and it also supports advanced usages like group variable selection and nuisance variable selection.
	"""
	
	cran = "bestridge" 

	version("1.0.7", md5="802ddd52ff23bde7561c2c647aef26e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.2.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
