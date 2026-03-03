# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomuniformforest(RPackage):
	"""Random Uniform Forests for Classification, Regression and
Unsupervised Learning

	Ensemble model, for classification, regression
	and unsupervised learning, based on a forest of unpruned 
	and randomized binary decision trees. Each tree is grown 
	by sampling, with replacement, a set of variables at each node. 
	Each cut-point is generated randomly, according to the continuous 
	Uniform distribution. For each tree, data are either bootstrapped 
	or subsampled. The unsupervised mode introduces clustering, dimension reduction
	and variable importance, using a three-layer engine. Random Uniform Forests are mainly 
	aimed to lower correlation between trees (or trees residuals), to provide a deep analysis 
	of variable importance and to allow native distributed and incremental learning.
	"""
	
	cran = "randomUniformForest" 

	version("1.1.6", md5="d6ce2a2b9214428c040cddbb934f76a7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-foreach@1.4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
