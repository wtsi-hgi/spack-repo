# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniSurvivalTree(RPackage):
	"""A Survival Tree Based on Stabilized Score Tests for
High-dimensional Covariates

	A classification (decision) tree is constructed from survival data with high-dimensional covariates.
 The method is a robust version of the logrank tree, where the variance is stabilized.
 The main function "uni.tree" returns a classification tree for a given survival dataset.
 The inner nodes (splitting criterion) are selected by minimizing the P-value of the two-sample the score tests.
 The decision of declaring terminal nodes (stopping criterion) is the P-value threshold given by an argument (specified by user).
 This tree construction algorithm is proposed by Emura et al. (2021, in review).
	"""
	
	cran = "uni.survival.tree" 

	version("1.5", md5="31b039047861c15acf0a3612fbd3a87b")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-compound-cox", type=("build", "run"))
