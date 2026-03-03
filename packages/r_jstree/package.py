# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJstree(RPackage):
	"""Create Interactive Trees with the 'jQuery' 'jsTree' Plugin

	Create and customize interactive trees using the
       'jQuery' 'jsTree' <https://www.jstree.com/> plugin
       library and the 'htmlwidgets' package. These trees can
       be used directly from the R console, from 'RStudio', in
       Shiny apps and R Markdown documents.
	"""
	
	homepage = "https://github.com/yonicd/jsTree"
	cran = "jsTree" 

	version("1.2", md5="735e51010d8d8af977b0f41259b279be")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
