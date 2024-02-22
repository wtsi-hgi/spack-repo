# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaptree(RPackage):
	"""Mapping, Pruning, and Graphing Tree Models

	Functions with example data for graphing, pruning, and
        mapping models from hierarchical clustering, and classification
        and regression trees.
	"""
	
	cran = "maptree" 

	version("1.4-8", md5="8db023baa8f3000ff384d846cb0d4815")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
