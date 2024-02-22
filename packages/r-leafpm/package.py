# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafpm(RPackage):
	"""Leaflet Map Plugin for Drawing and Editing

	A collection of tools for interactive manipulation of (spatial) data 
    layers on leaflet web maps. Tools include editing of existing layers, creation 
    of new layers through drawing of shapes (points, lines, polygons), deletion 
    of shapes as well as cutting holes into existing shapes. Provides control over 
    options to e.g. prevent self-intersection of polygons and lines or to enable/disable 
    snapping to align shapes.
	"""
	
	homepage = "https://github.com/r-spatial/leafpm"
	cran = "leafpm" 

	version("0.1.0", md5="ab8f4f6a53857966a9fffda1aaa7d7f4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools@0.3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-leaflet@2.0.1:", type=("build", "run"))
	depends_on("r-sf@0.5.2:", type=("build", "run"))
