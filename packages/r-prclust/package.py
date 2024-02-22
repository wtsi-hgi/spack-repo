# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrclust(RPackage):
	"""Penalized Regression-Based Clustering Method

	Clustering is unsupervised and exploratory in nature. Yet, it can be performed through penalized regression with grouping pursuit. In this package, we provide two algorithms for fitting the penalized regression-based clustering (PRclust) with non-convex grouping penalties, such as group truncated lasso, MCP and SCAD. One algorithm is based on quadratic penalty and difference convex method. Another algorithm is based on difference convex and ADMM, called DC-ADD, which is more efficient. Generalized cross validation and stability based method were provided to select the tuning parameters. Rand index, adjusted Rand index and Jaccard index were provided to estimate the agreement between estimated cluster memberships and the truth.
	"""
	
	cran = "prclust" 

	version("1.3", md5="f1c879f3a87f2bbcee042fdd68150368")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
