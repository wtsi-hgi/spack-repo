# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWcluster(RPackage):
	"""Clustering and PCA with Weights, and Data Nuggets Clustering

	K-means clustering, hierarchical clustering, and PCA with observational 
    weights and/or variable weights. It also includes the corresponding functions 
    for data nuggets which serve as representative samples of large datasets.
    Cherasia et al., (2022) <doi:10.1007/978-3-031-22687-8_20>. 
    Amaratunga et al., (2009) <doi:10.1002/9780470317129>.
	"""
	
	cran = "WCluster" 

	version("1.2.0", md5="4974ef845593b9e5f35707537426da6c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-datanugget@1.2.2:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
