# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsopam(RPackage):
	"""Clustering of Sites with Species Data

	Clustering algorithm developed for use with plot inventories of species. It groups plots by subsets of diagnostic species rather than overall species composition. There is an unsupervised and a supervised mode, the latter accepting suggestions for species with greater weight and cluster medoids. 
	"""
	
	cran = "isopam" 

	version("2.0", md5="34710eccb0bda75054b770353dc8a08c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
