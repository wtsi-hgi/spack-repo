# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraph3d(RPackage):
	"""A Wrapper of the JavaScript Library 'vis-graph3d'

	Create interactive visualization charts to draw data in three dimensional graphs. The graphs can be included in Shiny apps and R markdown documents, or viewed from the R console and 'RStudio' Viewer. Based on the 'vis.js' Graph3d module and the 'htmlwidgets' R package.
	"""
	
	homepage = "https://github.com/stla/graph3d"
	cran = "graph3d" 

	version("0.2.0", md5="bc3a47ee0d4cb6f29d0a976244f7bb88")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
