# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJstreer(RPackage):
	"""A Wrapper of the JavaScript Library 'jsTree'

	Creates interactive trees that can be included in 'Shiny'
    apps and R markdown documents. A tree allows to represent hierarchical
    data (e.g. the contents of a directory). Similar to the 'shinyTree'
    package but offers more features and options, such as the grid
    extension, restricting the drag-and-drop behavior, and settings for
    the search functionality. It is possible to attach some data to the
    nodes of a tree and then to get these data in 'Shiny' when a node is
    selected. Also provides a 'Shiny' gadget allowing to manipulate one or
    more folders, and a 'Shiny' module allowing to navigate in the server
    side file system.
	"""
	
	homepage = "https://github.com/stla/jsTreeR"
	cran = "jsTreeR" 

	version("2.5.0", md5="38bc6161dd93fdd7493a477c0a790c92")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jquerylib", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
