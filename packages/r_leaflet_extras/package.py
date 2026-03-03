# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafletExtras(RPackage):
	"""Extra Functionality for 'leaflet' Package

	The 'leaflet' JavaScript library provides many plugins some of which
    are available in the core 'leaflet' package, but there are many more. It is not
    possible to support them all in the core 'leaflet' package. This package serves
    as an add-on to the 'leaflet' package by providing extra functionality via 'leaflet'
    plugins.
	"""
	
	homepage = "https://github.com/bhaskarvk/leaflet.extras"
	cran = "leaflet.extras" 

	version("1.0.0", md5="ece4bf7634e9bea62b284a1b4dffa4d3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
