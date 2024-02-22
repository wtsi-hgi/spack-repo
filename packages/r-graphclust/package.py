# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphclust(RPackage):
	"""Hierarchical Graph Clustering for a Collection of Networks

	Graph clustering using an agglomerative algorithm to maximize the
  integrated classification likelihood criterion and a mixture of stochastic
  block models. The method is described in the article "Model-based clustering 
  of multiple networks with a hierarchical algorithm" by 
  T. Rebafka (2022) <arXiv:2211.02314>.
	"""
	
	cran = "graphclust" 

	version("1.3", md5="9aadfe94543569a05231bb2be7886ad1")

	depends_on("r-blockmodels", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sclust", type=("build", "run"))
