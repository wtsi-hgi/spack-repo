# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnahelper(RPackage):
	"""'RStudio' Addin for Network Analysis and Visualization

	'RStudio' addin which provides a GUI to visualize and analyse networks. 
    After finishing a session, the code to produce the plot is inserted in the current script.
    Alternatively, the function SNAhelperGadget() can be used directly from the console.
    Additional addins include the Netreader() for reading network files, Netbuilder() to create
    small networks via point and click, and the Componentlayouter() to layout networks with many components manually.
	"""
	
	homepage = "https://github.com/schochastics/snahelper"
	cran = "snahelper" 

	version("1.4.2", md5="1d8c5efaef960462a6568212b1f787b0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggraph@2:", type=("build", "run"))
	depends_on("r-graphlayouts@0.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
