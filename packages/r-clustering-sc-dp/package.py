# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusteringScDp(RPackage):
	"""Optimal Distance-Based Clustering for Multidimensional Data with
Sequential Constraint

	A dynamic programming algorithm for optimal clustering multidimensional data with sequential constraint. The algorithm minimizes the sum of squares of within-cluster distances. The sequential constraint allows only subsequent items of the input data to form a cluster. The sequential constraint is typically required in clustering data streams or items with time stamps such as video frames, GPS signals of a vehicle, movement data of a person, e-pen data, etc. The algorithm represents an extension of 'Ckmeans.1d.dp' to multiple dimensional spaces. Similarly to the one-dimensional case, the algorithm guarantees optimality and repeatability of clustering. Method clustering.sc.dp() can find the optimal clustering if the number of clusters is known. Otherwise, methods findwithinss.sc.dp() and backtracking.sc.dp() can be used. See Szkaliczki, T. (2016) "clustering.sc.dp: Optimal Clustering with Sequential Constraint by Using Dynamic Programming" <doi: 10.32614/RJ-2016-022> for more information.
	"""
	
	cran = "clustering.sc.dp" 

	version("1.1", md5="39d6bf1e50d652778f4d1327b74683b4")

	depends_on("r@2.10:", type=("build", "run"))
