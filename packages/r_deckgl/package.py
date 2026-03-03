# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeckgl(RPackage):
	"""An R Interface to 'deck.gl'

	Makes 'deck.gl' <https://deck.gl/>, a WebGL-powered open-source JavaScript framework
  for visual exploratory data analysis of large datasets, available within R via the 'htmlwidgets' package.
  Furthermore, it supports basemaps from 'mapbox' <https://www.mapbox.com/> via
  'mapbox-gl-js' <https://github.com/mapbox/mapbox-gl-js>.
	"""
	
	homepage = "https://github.com/crazycapivara/deckgl/"
	cran = "deckgl" 

	version("0.3.0", md5="f83a6617e49658a9fe3ab18eb76b0130")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
