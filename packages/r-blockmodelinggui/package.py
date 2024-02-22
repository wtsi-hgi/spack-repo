# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockmodelinggui(RPackage):
	"""GUI for the Generalised Blockmodeling of Valued Networks

	This app provides some useful tools for Offering an accessible GUI for generalised blockmodeling of single-relation, one-mode networks. The user can execute blockmodeling without having to write a line code by using the app's visual helps. Moreover, there are several ways to visualisations networks and their partitions. Finally, the results can be exported as if they were produced by writing code. The development of this package is financially supported by the Slovenian Research Agency (www.arrs.gov.si) within the research project J5-2557 (Comparison and evaluation of different approaches to blockmodeling dynamic networks by simulations with application to Slovenian co-authorship networks).
	"""
	
	cran = "BlockmodelingGUI" 

	version("1.8.4", md5="9c890734881a22a08f734ea1574e18ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-blockmodeling", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
