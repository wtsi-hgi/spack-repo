# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMergetrees(RPackage):
	"""Aggregating Trees

	Aggregates a set of trees with the same leaves to create a consensus tree. The trees are typically 
  obtained via hierarchical clustering, hence the hclust format is used to encode both the aggregated trees and the final 
  consensus tree. The method is exact and proven to be O(nqlog(n)), n being the individuals and q being the number of trees to aggregate.
	"""
	
	cran = "mergeTrees" 

	version("0.1.3", md5="391b5b2dbec84fb9fff4647c8e4cbae5")

	depends_on("r-rcpp", type=("build", "run"))
