# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeonetwork(RPackage):
	"""Geographic Networks

	Provides classes and methods for handling networks or 
  graphs whose nodes are geographical (i.e. locations in the globe).
  The functionality includes the creation of objects of class geonetwork
  as a graph with node coordinates, the computation of network measures,
  the support of spatial operations (projection to different Coordinate
  Reference Systems, handling of bounding boxes, etc.) and the plotting of
  the geonetwork object combined with supplementary cartography for spatial 
  representation.
	"""
	
	homepage = "https://umr-astre.pages.mia.inra.fr/geonetwork"
	cran = "geonetwork" 

	version("0.5.0", md5="a1e66131f6d6af0f04db29c89f6a198d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
