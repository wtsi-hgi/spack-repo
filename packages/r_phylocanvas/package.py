# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylocanvas(RPackage):
	"""Interactive Phylogenetic Trees Using the 'Phylocanvas'
JavaScript Library

	Create and customize interactive phylogenetic trees using the 'phylocanvas' JavaScript library and the 'htmlwidgets' package. These trees can be used directly from the R console, from 'RStudio', in Shiny apps, and in R Markdown documents.  See <http://phylocanvas.org/>  for more information on the 'phylocanvas' library.
	"""
	
	homepage = "https://github.com/zachcp/phylocanvas"
	cran = "phylocanvas" 

	version("0.1.3", md5="7cfe07615ee367e56f0afc76aae9f28a")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-ape@4:", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
