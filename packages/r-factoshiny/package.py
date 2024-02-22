# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactoshiny(RPackage):
	"""Perform Factorial Analysis from 'FactoMineR' with a Shiny
Application

	Perform factorial analysis with a menu and draw graphs interactively thanks to 'FactoMineR' and a Shiny application.
	"""
	
	homepage = "http://factominer.free.fr/graphs/factoshiny.html"
	cran = "Factoshiny" 

	version("2.5", md5="42f62d1fc6bd374879f0cb1d4cfc3214")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-factominer@2.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-factoinvestigate@1.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-missmda", type=("build", "run"))
