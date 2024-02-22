# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoa(RPackage):
	"""Lattice Options and Add-Ins

	Various plots and functions that make use of the lattice/trellis plotting framework. 
   The plots, which include loaPlot(), RgoogleMapsPlot() and trianglePlot(), use panelPal(), a function that 
   extends 'lattice' and 'hexbin' package methods to automate plot subscript and panel-to-panel 
   and panel-to-key synchronization/management.   
	"""
	
	homepage = "http://loa.r-forge.r-project.org/loa.intro.html"
	cran = "loa" 

	version("0.2.48.3", md5="a20193d20ff4873ea3ce5b57030618ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rgooglemaps", type=("build", "run"))
	depends_on("r-openstreetmap", type=("build", "run"))
	depends_on("r-sp@2.1.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
