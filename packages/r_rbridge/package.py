# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbridge(RPackage):
	"""Restricted Bridge Estimation

	Bridge Regression estimation with linear restrictions defined in Yuzbasi et al. (2019) <arXiv:1910.03660>. Special cases of this approach fit the restricted LASSO, restricted RIDGE and restricted Elastic Net estimators.
	"""
	
	cran = "rbridge" 

	version("1.0.2", md5="cfd1d87c292c36c16fdb471d313e851a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
