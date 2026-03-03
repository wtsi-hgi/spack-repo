# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRanktreeensemble(RPackage):
	"""Ensemble Models of Rank-Based Trees with Extracted Decision
Rules

	Fast computing an ensemble of rank-based trees via boosting or random forest on binary and multi-class problems. It converts continuous gene expression profiles into ranked gene pairs, for which the variable importance indices are computed and adopted for dimension reduction. Decision rules can be extracted from trees. 
	"""
	
	homepage = "https://github.com/TransBioInfoLab/ranktreeEnsemble/"
	cran = "ranktreeEnsemble" 

	version("0.22", md5="c0f38226be4110476d748dfc125ade59")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
