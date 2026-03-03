# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmap(RPackage):
	"""Thematic Maps

	Thematic maps are geographical maps in which spatial data distributions are visualized. This package offers a flexible, layer-based, and easy to use approach to create thematic maps, such as choropleths and bubble maps.
	"""
	
	homepage = "https://r-tmap.github.io/tmap/"
	cran = "tmap" 

	version("3.3-4", md5="d22384d2348d9f344fbecf6d8b8f42c5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmaptools@3.1:", type=("build", "run"))
	depends_on("r-sf@0.9.7:", type=("build", "run"))
	depends_on("r-stars@0.5.0:", type=("build", "run"))
	depends_on("r-units@0.6.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-classint@0.4.3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-widgetframe", type=("build", "run"))
	depends_on("r-leaflet@2.0.2:", type=("build", "run"))
	depends_on("r-leafsync", type=("build", "run"))
	depends_on("r-leafem@0.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
