# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeadercluster(RPackage):
	"""Leader Clustering Algorithm

	The leader clustering algorithm provides
 a means for clustering a set of data points. Unlike many other clustering
 algorithms it does not require the user to specify the number of clusters,
 but instead requires the approximate radius of a cluster as its primary
 tuning parameter. The package provides a fast implementation of this
 algorithm in n-dimensions using Lp-distances (with special cases for p=1,2,
 and infinity) as well as for spatial data using the Haversine
 formula, which takes latitude/longitude pairs as inputs and clusters
 based on great circle distances.
	"""
	
	cran = "leaderCluster" 

	version("1.5", md5="c2341718cd71ca5c46d663c45fbf5a22")

