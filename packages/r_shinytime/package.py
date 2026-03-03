# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytime(RPackage):
	"""A Time Input Widget for Shiny

	Provides a time input widget for Shiny. This widget allows intuitive time input in the
    '[hh]:[mm]:[ss]' or '[hh]:[mm]' (24H) format by using a separate numeric input for each time
    component. The interface with R uses date-time objects. See the project page for more
    information and examples.
	"""
	
	homepage = "https://burgerga.github.io/shinyTime/"
	cran = "shinyTime" 

	version("1.0.3", md5="d244fb3323dfb8fb15ac3f61fac8ab2c")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
