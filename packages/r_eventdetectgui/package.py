# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventdetectgui(RPackage):
	"""Graphical User Interface for the 'EventDetectR' Package

	A graphical user interface for open source event detection.
	"""
	
	cran = "EventDetectGUI" 

	version("0.3.0", md5="0022d91fe209f04b54c12d9b6e51a5f1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-eventdetectr", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
