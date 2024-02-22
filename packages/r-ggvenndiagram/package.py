# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgvenndiagram(RPackage):
	"""A 'ggplot2' Implement of Venn Diagram

	Easy-to-use functions to generate 2-7 sets Venn or upset plot in publication quality. 
  'ggVennDiagram' plot Venn or upset using well-defined geometry dataset and 'ggplot2'. The shapes of 2-4 sets 
  Venn use circles and ellipses, while the shapes of 4-7 sets Venn use irregular polygons (4 has both forms), which 
  are developed and imported from another package 'venn', authored by Adrian Dusa. We provided internal functions to 
  integrate shape data with user provided sets data, and calculated the geometry of every regions/intersections 
  of them, then separately plot Venn in four components, set edges/labels, and region edges/labels.
  From version 1.0, it is possible to customize these components as you demand in ordinary 'ggplot2' grammar.
  From version 1.4.4, it supports unlimited number of sets, as it can draw a plain upset plot automatically when
  number of sets is more than 7.
	"""
	
	homepage = "https://github.com/gaospecial/ggVennDiagram"
	cran = "ggVennDiagram" 

	version("1.5.2", md5="25718bbd19e6bf11b4dea69609664d64")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-venn@1.12:", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
