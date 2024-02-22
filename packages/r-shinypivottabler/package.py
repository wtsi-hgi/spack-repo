# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinypivottabler(RPackage):
	"""Shiny Module to Create Pivot Tables

	Shiny Module to create, visualize, customize and export Excel-like pivot table.
	"""
	
	cran = "shinypivottabler" 

	version("1.2", md5="e8fadad60aea09dab63016f63cbcfb00")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pivottabler@1.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
