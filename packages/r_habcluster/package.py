# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHabcluster(RPackage):
	"""Detecting Spatial Clustering Based on Connection Cost Between
Grids

	Based on landscape connectivity, spatial boundaries were
        identified using community detection algorithm at grid level. Methods 
        using raster as input and the value of each cell of the raster is the 
        "smoothness" to indicate how easy the cell connecting with neighbor cells. 
        Details about the 'habCluster' package methods can be found in Zhang et al.
        <bioRxiv:2022.05.06.490926>.
	"""
	
	cran = "habCluster" 

	version("1.0.5", md5="5943a814be8aa8ea1efda730f8bdaa2b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph@1.3:", type=("build", "run"))
	depends_on("r-stars@0.5.0:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
