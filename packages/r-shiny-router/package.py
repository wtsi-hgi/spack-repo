# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyRouter(RPackage):
	"""Basic Routing for Shiny Web Applications

	It is a simple router for your Shiny apps.
    The router allows you to create dynamic web applications with real-time
    User Interface and easily share url to pages within your Shiny apps.
	"""
	
	homepage = "https://appsilon.github.io/shiny.router/"
	cran = "shiny.router" 

	version("0.3.1", md5="4f95bd494a1e55efc2e34680aab81080")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
