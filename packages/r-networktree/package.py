# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworktree(RPackage):
	"""Recursive Partitioning of Network Models

	Network trees recursively partition the data with respect to covariates. Two network tree algorithms are available: model-based trees based on a multivariate normal model and nonparametric trees based on covariance structures. After partitioning, correlation-based networks (psychometric networks) can be fit on the partitioned data. For details see Jones, Mair, Simon, & Zeileis (2020) <doi:10.1007/s11336-020-09731-4>. 
	"""
	
	homepage = "https://paytonjjones.github.io/networktree/"
	cran = "networktree" 

	version("1.0.1", md5="4152624f648a2baf0d43107728a563f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
