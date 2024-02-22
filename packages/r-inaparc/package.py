# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInaparc(RPackage):
	"""Initialization Algorithms for Partitioning Cluster Analysis

	Partitioning clustering algorithms divide data sets into k subsets or partitions so-called clusters. They require some initialization procedures for starting the algorithms. Initialization of cluster prototypes is one of such kind of procedures for most of the partitioning algorithms. Cluster prototypes are the centers of clusters, i.e. centroids or medoids, representing the clusters in a data set. In order to initialize cluster prototypes, the package 'inaparc' contains a set of the functions that are the implementations of several linear time-complexity and loglinear time-complexity methods in addition to some novel techniques. Initialization of fuzzy membership degrees matrices is another important task for starting the probabilistic and possibilistic partitioning algorithms. In order to initialize membership degrees matrices required by these algorithms, a number of functions based on some traditional and novel initialization techniques are also available in the package 'inaparc'.
	"""
	
	cran = "inaparc" 

	version("1.2.0", md5="7cd222982dd94510d0f4e1c1e1f4d6ac")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-kpeaks", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
