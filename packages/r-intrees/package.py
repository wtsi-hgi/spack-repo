# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrees(RPackage):
	"""Interpret Tree Ensembles

	For tree ensembles such as random forests, regularized random forests and gradient boosted trees, this package provides functions for: extracting, measuring and pruning rules; selecting a compact rule set; summarizing rules into a learner; calculating frequent variable interactions; formatting rules in latex code.  Reference: Interpreting tree ensembles with inTrees (Houtao Deng, 2019, <doi:10.1007/s41060-018-0144-8>).
	"""
	
	cran = "inTrees" 

	version("1.3", md5="aacf148c1150646d8e5a3279d2ac064d")

	depends_on("r-rrf", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
