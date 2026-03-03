# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemdrw(RPackage):
	"""'SEM Shiny'

	Interactive 'shiny' application for working with Structural Equation Modelling technique. Runtime examples are provided in the package function as well as at  <https://kartikeyab.shinyapps.io/semwebappk/> .
	"""
	
	cran = "semdrw" 

	version("0.1.0", md5="cf360bed84b8c3a6986babd25a1c41a3")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-semtools", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
