# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLareshiny(RPackage):
	"""Lares 'shiny' Modules

	Useful 'shiny' production-ready modules and helpers such as login window and visualization tools.
	"""
	
	homepage = "https://github.com/laresbernardo/lareshiny"
	cran = "lareshiny" 

	version("0.0.3", md5="5384325d3c419219aab94fb336499483")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
