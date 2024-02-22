# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGimmetools(RPackage):
	"""Supplemental Tools for the 'gimme' R Package

	Supplemental tools for the 'gimme' R package. It contains an interactive graphical user interface, allowing for the flexible specification of a variety of both basic and advanced options. It will expand to include a variety of tools for navigating output.
	"""
	
	homepage = "https://github.com/stlane"
	cran = "gimmeTools" 

	version("0.1", md5="d13d9a6ee1f95526ad29f1a6d705d3e0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-easycsv", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
