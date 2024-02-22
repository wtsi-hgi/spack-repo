# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootcluster(RPackage):
	"""Bootstrapping Estimates of Clustering Stability

	Implementation of the bootstrapping approach for the estimation of clustering stability and its application in estimating the number of clusters, as introduced by Yu et al (2016)<doi:10.1142/9789814749411_0007>. Implementation of the non-parametric bootstrap approach to assessing the stability of module detection in a graph, the extension for the selection of a parameter set that defines a graph from data in a way that optimizes stability and the corresponding visualization functions, as introduced by Tian et al (2021) <doi:10.1002/sam.11495>.
	"""
	
	cran = "bootcluster" 

	version("0.3.2", md5="fdec42b89978aae421b53cb5b3d53190")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
