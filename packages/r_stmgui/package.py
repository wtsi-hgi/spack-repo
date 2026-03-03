# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStmgui(RPackage):
	"""Shiny Application for Creating STM Models

	Provides an application that acts as a GUI for the 'stm' text analysis package.
	"""
	
	cran = "stmgui" 

	version("0.1.6", md5="1769d127ae9b1ad3743e901357153680")

	depends_on("r-stm", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
