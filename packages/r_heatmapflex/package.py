# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatmapflex(RPackage):
	"""Tools to Generate Flexible Heatmaps

	A set of tools supporting more flexible heatmaps. The graphics is grid-like using
  the old graphics system. The main function is heatmap.n2(), which is a wrapper around the various functions
  constructing individual parts of the heatmap, like sidebars, picket plots, legends etc. The function supports zooming
  and splitting, i.e., having (unlimited) small heatmaps underneath each other in one plot deriving from the same data set,
  e.g., clustered and ordered by a supervised clustering method.
	"""
	
	cran = "heatmapFlex" 

	version("0.1.2", md5="b2620f028269a3e4e7b8465aef694bb2")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-heatplus", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
