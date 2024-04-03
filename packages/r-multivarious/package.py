# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivarious(RPackage):
	"""Extensible Data Structures for Multivariate Analysis

	Provides a set of basic and extensible data structures and functions for multivariate analysis, including dimensionality reduction techniques, projection methods, and preprocessing functions. The aim of this package is to offer a flexible and user-friendly framework for multivariate analysis that can be easily extended for custom requirements and specific data analysis tasks.
	"""
	
	homepage = "https://bbuchsbaum.github.io/multivarious/"
	cran = "multivarious" 

	version("0.2.0", md5="c664b036d88cbc2e0232691030fed332")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
