# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUmatrix(RPackage):
	"""Visualization of Structures in High-Dimensional Data

	By gaining the property of emergence through self-organization, the enhancement of SOMs(self organizing maps) is called Emergent SOM (ESOM). The result of the projection by ESOM is a grid of neurons which can be visualised as a three dimensional landscape in form of the Umatrix. Further details can be found in the referenced publications (see url). This package offers tools for calculating and visualising the ESOM as well as Umatrix, Pmatrix and UStarMatrix. All the functionality is also available through graphical user interfaces implemented in 'shiny'.
	"""
	
	homepage = "http://wscg.zcu.cz/wscg2016/short/A43-full.pdf"
	cran = "Umatrix" 

	version("3.4.1", md5="224b1c95f442db35cf9541fe421a5ac1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-adaptgauss", type=("build", "run"))
	depends_on("r-datavisualizations", type=("build", "run"))
