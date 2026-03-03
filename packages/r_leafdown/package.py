# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafdown(RPackage):
	"""Provides Drill Down Functionality for 'leaflet' Choropleths

	Provides drill down functionality for 'leaflet' choropleths in 'shiny' apps.
	"""
	
	cran = "leafdown" 

	version("1.2.0", md5="22d7bce2adb0ba8d46692ff90fea6f24")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
