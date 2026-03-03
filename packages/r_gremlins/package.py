# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGremlins(RPackage):
	"""Generalized Multipartite Networks

	We define generalized multipartite networks  as the joint observation of several networks implying some common pre-specified groups of individuals. The aim is to fit an adapted version of  the popular stochastic block model to multipartite networks, as described in Bar-hen, Barbillon and Donnet (2020) <arXiv:1807.10138>.  
	"""
	
	homepage = "https://GrossSBM.github.io/GREMLINS/"
	cran = "GREMLINS" 

	version("0.2.1", md5="4425cbcaf553fe03dc64c5b01289e8cc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-blockmodels", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
