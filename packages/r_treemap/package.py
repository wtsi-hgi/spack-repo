# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreemap(RPackage):
	"""Treemap Visualization

	A treemap is a space-filling visualization of hierarchical
    structures. This package offers great flexibility to draw treemaps.
	"""
	
	cran = "treemap" 

	version("2.4-4", md5="2113bbaede39f911191c18878c45dadc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-data-table@1.8.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shiny@0.12:", type=("build", "run"))
