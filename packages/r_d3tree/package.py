# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD3tree(RPackage):
	"""Create Interactive Collapsible Trees with the JavaScript 'D3'
Library

	Create and customize interactive collapsible 'D3' trees using the 'D3'
    JavaScript library and the 'htmlwidgets' package. These trees can be used
    directly from the R console, from 'RStudio', in Shiny apps and R Markdown documents.
    When in Shiny the tree layout is observed by the server and can be used as a reactive filter
    of structured data.
	"""
	
	homepage = "https://github.com/yonicd/d3Tree"
	cran = "d3Tree" 

	version("0.3.0", md5="06678baedbd4bd2d71b342471710e4d3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
