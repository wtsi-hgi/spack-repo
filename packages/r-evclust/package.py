# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvclust(RPackage):
	"""Evidential Clustering

	Various clustering algorithms that produce a credal partition,
    i.e., a set of Dempster-Shafer mass functions representing the membership of objects
    to clusters. The mass functions quantify the cluster-membership uncertainty of the     
    objects. The algorithms are: Evidential c-Means, Relational Evidential c-Means, 
    Constrained Evidential c-Means, Evidential Clustering, Constrained Evidential 
    Clustering, Evidential K-nearest-neighbor-based Clustering, Bootstrap Model-Based
    Evidential Clustering, Belief Peak Evidential Clustering, Neural-Network-based
    Evidential Clustering. 
	"""
	
	cran = "evclust" 

	version("2.0.3", md5="c8c42ebeb878e420783ed3e8e64ed214")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
