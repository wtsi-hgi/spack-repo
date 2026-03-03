# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirectedclustering(RPackage):
	"""Directed Weighted Clustering Coefficient

	Allows the computation of clustering coefficients for directed and weighted networks by using different approaches. 
    It allows to compute clustering coefficients that are not present in 'igraph' package. 
    A description of clustering coefficients can be found in "Directed clustering in weighted networks: a new perspective", Clemente, G.P., Grassi, R. (2017),  	
    <doi:10.1016/j.chaos.2017.12.007>.
	"""
	
	cran = "DirectedClustering" 

	version("0.1.1", md5="f30ebfb8b978f42b9cd1998e16fcda8c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
