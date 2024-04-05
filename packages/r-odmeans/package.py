# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdmeans(RPackage):
	"""OD-Means: k-Means for Origin-Destination

	OD-means is a hierarchical adaptive k-means algorithm based on origin-destination pairs. 
    In the first layer of the hierarchy, the clusters are separated automatically based on the variation 
    of the within-cluster distance of each cluster until convergence. The second layer of the hierarchy 
    corresponds to the sub clustering process of small clusters based on the distance between the origin 
    and destination of each cluster.
	"""
	
	cran = "ODMeans" 

	version("0.2.1", md5="d2a595e99b85e6931d266faef3c53b73")
	version("0.2.0", md5="4155dab4f8f479b17ce41d96ceb0b9f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
