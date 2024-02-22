# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputer(RPackage):
	"""A General Multivariate Imputation Framework

	Multivariate Expectation-Maximization (EM) based imputation framework that offers several different algorithms. These include regularisation methods like Lasso and Ridge regression, tree-based models and dimensionality reduction methods like PCA and PLS.
	"""
	
	homepage = "http://github.com/SteffenMoritz/imputeR"
	cran = "imputeR" 

	version("2.2", md5="3f357c3ca26fbed206c6acabc8cbb403")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
