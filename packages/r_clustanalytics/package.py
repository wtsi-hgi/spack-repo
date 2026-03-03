# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustanalytics(RPackage):
	"""Cluster Evaluation on Graphs

	Evaluates the stability and significance of clusters on 'igraph' graphs.
    Supports weighted and unweighted graphs. Implements the cluster evaluation methods
    defined by Arratia A, Renedo M (2021) <doi:10.7717/peerj-cs.600>. Also includes an
    implementation of the Reduced Mutual Information introduced by Newman et al. (2020) 
    <doi:10.1103/PhysRevE.101.042304>.
	"""
	
	homepage = "https://github.com/martirm/clustAnalytics"
	cran = "clustAnalytics" 

	version("0.5.5", md5="01db97556f3a6fb4b823bdf146f40c7f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mcclust", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-fossil", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
