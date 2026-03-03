# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinycyjs(RPackage):
	"""Create Interactive Network Visualizations in R and 'shiny'

	Create Interactive Graph (Network) Visualizations. 
  'shinyCyJS' can be used in 'Shiny' apps or viewed from 'Rstudio' Viewer.
  'shinyCyJS' includes API to build Graph model like node or edge with customized attributes for R. 
  'shinyCyJS' is built with 'cytoscape.js' and 'htmlwidgets' R package.
	"""
	
	homepage = "https://github.com/jhk0530/shinyCyJS"
	cran = "shinyCyJS" 

	version("1.0.0", md5="b7023efef10fa2aa012650b4246ca2d4")

	depends_on("r-htmlwidgets", type=("build", "run"))
