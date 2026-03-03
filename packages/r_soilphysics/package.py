# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilphysics(RPackage):
	"""Soil Physical Analysis

	Basic and model-based soil physical analyses.
	"""
	
	homepage = "https://arsilva87.github.io/soilphysics/"
	cran = "soilphysics" 

	version("5.0", md5="c46f54ae6e9aa08286f50917942f7314")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
