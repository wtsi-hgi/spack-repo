# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridstacker(RPackage):
	"""Wrapper for 'gridstack.js'

	An easy way to create responsive layouts with just a few lines of code. You can create boxes that are draggable and resizable and load predefined Layouts. The package serves as a wrapper to allow for easy integration of the 'gridstack.js' functionalities <https://github.com/gridstack/gridstack.js>. 
	"""
	
	cran = "gridstackeR" 

	version("0.1.0", md5="37c8c8537e9c0cb688a83967646bec83")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
