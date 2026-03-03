# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeclust(RPackage):
	"""Cluster Distances Through Trees

	Create a measure of inter-point dissimilarity useful 
 for clustering mixed data, and, optionally, perform the clustering.
	"""
	
	cran = "treeClust" 

	version("1.1-7", md5="baf382265ed21048059bda6a3be2e925")

	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
