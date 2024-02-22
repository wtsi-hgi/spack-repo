# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmvgraph(RPackage):
	"""Various Multivariate Graphics with Variable Choice in Shiny Apps

	Mosaic diagram, scatterplot matrix, Andrews curves, parallel coordinate diagram, radar diagram, 
   and Chernoff plots as a Shiny app, which allow the order of variables to be changed interactively. 
   The apps are intended as teaching examples.
	"""
	
	cran = "smvgraph" 

	version("0.1.2", md5="e5c42cff17c21bfe8297829a1f903034")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-sortable", type=("build", "run"))
