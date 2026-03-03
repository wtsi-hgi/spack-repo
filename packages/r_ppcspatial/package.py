# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpcspatial(RPackage):
	"""Spatial Analysis of Pakistan Population Census

	Spatial Analysis for exploration of Pakistan Population Census 2017 (<https://www.pbs.gov.pk/content/population-census>). It uses data from R package 'PakPC2017'.
	"""
	
	homepage = "https://github.com/MYaseen208/ppcSpatial"
	cran = "ppcSpatial" 

	version("0.3.0", md5="2482d98bd09e3c31e52617be185641f6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pakpc2017", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
