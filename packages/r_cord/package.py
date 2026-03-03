# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCord(RPackage):
	"""Community Estimation in G-Models via CORD

	Partition data points (variables) into communities/clusters, similar to clustering algorithms, such as k-means and hierarchical clustering.  This package implements a clustering algorithm based on a new metric CORD, defined for high dimensional parametric or semi-parametric distributions.  Read http://arxiv.org/abs/1508.01939 for more details.
	"""
	
	cran = "cord" 

	version("0.1.1", md5="a86f17db3fe8a64fb56004d7d88437ef")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
