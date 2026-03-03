# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDclust(RPackage):
	"""Divisive Hierarchical Clustering

	Contains a single function dclust() for divisive hierarchical clustering based on 
    recursive k-means partitioning (k = 2). Useful for clustering large datasets
    where computation of a n x n distance matrix is not feasible (e.g. n > 10,000 records).
    For further information see Steinbach, Karypis and Kumar (2000) <http://glaros.dtc.umn.edu/gkhome/fetch/papers/docclusterKDDTMW00.pdf>.
	"""
	
	homepage = "http://github.com/shaunpwilkinson/dclust"
	cran = "dclust" 

	version("0.1.0", md5="7e1b1104a44bb2ab55d3123d6de34f51")

	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-phylogram", type=("build", "run"))
