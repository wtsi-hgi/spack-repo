# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollapsibletree(RPackage):
	"""Interactive Collapsible Tree Diagrams using 'D3.js'

	
    Interactive Reingold-Tilford tree diagrams created using 'D3.js', where every node can be expanded and collapsed by clicking on it.
    Tooltips and color gradients can be mapped to nodes using a numeric column in the source data frame.
    See 'collapsibleTree' website for more information and examples.
	"""
	
	homepage = "https://github.com/AdeelK93/collapsibleTree"
	cran = "collapsibleTree" 

	version("0.1.8", md5="d6526f3286e26f6e4144cd48f0952e26")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
