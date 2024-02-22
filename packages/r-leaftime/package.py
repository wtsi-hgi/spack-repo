# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeaftime(RPackage):
	"""'Leaflet-timeline' Plugin for Leaflet

	Use the 'leaflet-timeline' plugin with a leaflet widget to add an
    interactive slider with play, pause, and step buttons to explore temporal
    geographic spatial data changes.
	"""
	
	homepage = "https://github.com/timelyportfolio/leaftime"
	cran = "leaftime" 

	version("0.2.0", md5="961cda7452db8ac8c4e3009c8ac4f702")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
