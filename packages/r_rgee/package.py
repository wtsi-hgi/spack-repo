# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgee(RPackage):
	"""R Bindings for Calling the 'Earth Engine' API

	Earth Engine <https://earthengine.google.com/> client library for R. All
  of the 'Earth Engine' API classes, modules, and functions are made available. Additional
  functions implemented include importing (exporting) of Earth Engine spatial objects, 
  extraction of time series, interactive map display, assets management interface, 
  and metadata display. See <https://r-spatial.github.io/rgee/> for further details.
	"""
	
	homepage = "https://github.com/r-spatial/rgee/"
	cran = "rgee" 

	version("1.1.7", md5="0ec31c9da6e8b2ff5bd8a9e2430ae2fa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-reticulate@1.27:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-leaflet@2.0.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-leafem", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
