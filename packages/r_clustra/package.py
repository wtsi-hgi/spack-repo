# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustra(RPackage):
	"""Clustering Longitudinal Trajectories

	Clusters longitudinal trajectories over time (can be unequally 
    spaced, unequal length time series and/or partially overlapping series) on
    a common time axis. Performs k-means clustering on a single continuous 
    variable measured over time, where each mean is defined by a thin plate 
    spline fit to all points in a cluster. Distance is MSE across trajectory 
    points to cluster spline. Provides graphs of derived cluster splines, 
    silhouette plots, and Adjusted Rand Index evaluations of the number
    of clusters. Scales well to large data with multicore parallelism available
    to speed computation.
	"""
	
	cran = "clustra" 

	version("0.2.1", md5="d3c200812d959b599964d41321c8f20d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mixsim", type=("build", "run"))
