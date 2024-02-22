# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustering(RPackage):
	"""Techniques for Evaluating Clustering

	The design of this package allows us to run different clustering packages and compare the results between them, to determine which algorithm behaves best from the data provided.
	"""
	
	homepage = "https://github.com/laperez/clustering"
	cran = "Clustering" 

	version("1.7.7", md5="962a12fed30a5ca692bf6239af683f0f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-toordinal", type=("build", "run"))
