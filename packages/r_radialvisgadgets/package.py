# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadialvisgadgets(RPackage):
	"""Interactive Gadgets for Radial Visualization Approaches

	Shiny-based interactive gadgets of radial visualization methods and extensions thereof.
	"""
	
	homepage = "https://github.com/jmatute/RadialShinyGadgets"
	cran = "RadialVisGadgets" 

	version("0.2.0", md5="b8b0d460bcfdaa9508504b1ebdf9a5c2")

	depends_on("r-import", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shinyscreenshot", type=("build", "run"))
