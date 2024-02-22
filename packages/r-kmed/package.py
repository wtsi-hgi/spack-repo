# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmed(RPackage):
	"""Distance-Based k-Medoids

	Algorithms of distance-based k-medoids clustering: simple and fast 
  k-medoids, ranked k-medoids, and increasing number of clusters in k-medoids. 
  Calculate distances for mixed variable data such as Gower, Podani, Wishart, 
  Huang, Harikumar-PV, and Ahmad-Dey. Cluster validation applies internal and 
  relative criteria. The internal criteria includes silhouette index and shadow 
  values. The relative criterium applies bootstrap procedure producing a heatmap 
  with a flexible reordering matrix algorithm such as complete, ward, or average 
  linkages. The cluster result can be plotted in a marked barplot or pca biplot.
	"""
	
	cran = "kmed" 

	version("0.4.2", md5="f1013bfd927c87bd9f9b96c5f7565837")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
