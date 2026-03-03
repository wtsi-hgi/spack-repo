# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridgraphviz(RPackage):
	"""Drawing Graphs with 'grid'

	Functions for drawing node-and-edge graphs that have been 
              laid out by 'graphviz'.  This provides an alternative 
              rendering to that provided by the 'Rgraphviz' package, with
              two main advantages:  the rendering provided by 'gridGraphviz'
              should be more similar to what 'graphviz' itself would draw;
              and rendering with 'grid' allows for post-hoc customisations
              using the named viewports and grobs that 'gridGraphviz'
              produces.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/gridgraph/"
	cran = "gridGraphviz" 

	version("0.3-1", md5="db617f7b64211e57222af5826a513e32")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("graphviz", type=("build", "link", "run"))
