# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapboxer(RPackage):
	"""An R Interface to 'Mapbox GL JS'

	Makes 'Mapbox GL JS' <https://docs.mapbox.com/mapbox-gl-js/api/>,
  an open source JavaScript library that uses WebGL to render interactive maps,
  available within R via the 'htmlwidgets' package. Visualizations can be used from the R console,
  in R Markdown documents and in Shiny apps.
	"""
	
	homepage = "https://github.com/crazycapivara/mapboxer"
	cran = "mapboxer" 

	version("0.4.0", md5="913b974e553b457eadf1dc4fb869964b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
