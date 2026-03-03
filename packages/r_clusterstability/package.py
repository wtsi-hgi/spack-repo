# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterstability(RPackage):
	"""Assessment of Stability of Individual Objects or Clusters in
Partitioning Solutions

	Allows one to assess the stability of individual objects, clusters 
    and whole clustering solutions based on repeated runs of the K-means and K-medoids 
    partitioning algorithms.
	"""
	
	cran = "ClusterStability" 

	version("1.0.4", md5="63ff3c5e973e9e1a16cd02a99c7a738e")

	depends_on("r@2.2.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-copula@0.999:", type=("build", "run"))
	depends_on("r-weightedcluster", type=("build", "run"))
