# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBddwc(RPackage):
	"""Darwinizer: Darwin Core (DwC) Field Names Standardization

	The 'shiny' application 'bdDwC' makes biodiversity data field names Darwin Core compatible.
	"""
	
	cran = "bdDwC" 

	version("0.1.15", md5="9ffd680d96cb9a8f6574cc0a6833ff5f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
