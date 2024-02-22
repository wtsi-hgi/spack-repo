# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyeffects(RPackage):
	"""Customize Your Web Apps with Fancy Effects

	Add fancy CSS effects to your 'shinydashboards' or 'shiny' apps.
             100% compatible with 'shinydashboardPlus' and 'bs4Dash'.
	"""
	
	homepage = "https://github.com/RinteRface/shinyEffects"
	cran = "shinyEffects" 

	version("0.2.0", md5="41f3bef0ee0cf176384066fc012a4ec7")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
