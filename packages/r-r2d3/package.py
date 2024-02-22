# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2d3(RPackage):
	"""Interface to 'D3' Visualizations

	Suite of tools for using 'D3', a library for producing dynamic, interactive data
  visualizations. Supports translating objects into 'D3' friendly data structures, rendering
  'D3' scripts, publishing 'D3' visualizations, incorporating 'D3' in R Markdown, creating
  interactive 'D3' applications with Shiny, and distributing 'D3' based 'htmlwidgets' in R
  packages.
	"""
	
	homepage = "https://rstudio.github.io/r2d3/"
	cran = "r2d3" 

	version("0.2.6", md5="75d99555a24d9a133cdabe79309de7ab", url="https://cran.r-project.org/src/contrib/r2d3_0.2.6.tar.gz")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
