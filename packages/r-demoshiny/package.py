# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemoshiny(RPackage):
	"""Runs a 'Shiny' App as Demo or Lists All Demo 'Shiny' Apps

	Mimics the demo functionality for 'Shiny' apps in a package. Apps stored to the package subdirectory inst/shiny can be called by demoShiny(topic).
	"""
	
	cran = "demoShiny" 

	version("0.1", md5="742161b7187a3fbfa4296dd2e32fd1e8")

	depends_on("r-shiny", type=("build", "run"))
