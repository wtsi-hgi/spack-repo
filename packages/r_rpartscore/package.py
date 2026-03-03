# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpartscore(RPackage):
	"""Classification Trees for Ordinal Responses

	Recursive partitioning methods to build
        classification trees for ordinal responses within the CART
        framework. Trees are grown using the Generalized Gini
        impurity function, where the misclassification costs are given
        by the absolute or squared differences in scores assigned to
        the categories of the response. Pruning is based on the total
        misclassification rate or on the total misclassification cost.
	"""
	
	cran = "rpartScore" 

	version("1.0-2", md5="1b530ff5d1e6710d85762208ef09e3f4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
