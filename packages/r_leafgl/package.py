# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafgl(RPackage):
	"""High-Performance 'WebGl' Rendering for Package 'leaflet'

	Provides bindings to the 'Leaflet.glify' JavaScript library which extends the 'leaflet' JavaScript library to render large data in the browser using 'WebGl'.
	"""
	
	cran = "leafgl" 

	version("0.1.1", md5="513be2e162783c9c2831b1ac7dc41a7e")

	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonify", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
