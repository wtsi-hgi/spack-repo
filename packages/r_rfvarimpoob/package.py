# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfvarimpoob(RPackage):
	"""Unbiased Variable Importance for Random Forests

	Computes a novel variable importance for random forests: Impurity reduction importance scores for out-of-bag (OOB) data complementing the existing inbag Gini importance, see also <doi: 10.1080/03610926.2020.1764042>. 
    The Gini impurities for inbag and OOB data are combined in three different ways, after which the information gain is computed at each split.
    This gain is aggregated for each split variable in a tree and averaged across trees.
	"""
	
	cran = "rfVarImpOOB" 

	version("1.0.3", md5="d3ce31739698ac912e6ae25f3eb8f6e8")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-titanic", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
