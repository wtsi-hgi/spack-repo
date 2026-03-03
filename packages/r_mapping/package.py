# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapping(RPackage):
	"""Automatic Download, Linking, Manipulating Coordinates for Maps

	Maps are an important tool to visualise variables distribution across different spatial objects. The mapping process requires to link the data with coordinates and then generate the correspondent map. This package provide coordinates, linking and mapping functions for an automatic, flexible and easy approach of external functions. The package provides an easy, flexible and automatic unit. Geographical coordinates are provided in the package and automatically linked with the input data to generate maps with internal provided functions or external functions. Provide an easy, flexible and automatic approach to potentially download updated coordinates, to link statistical units with coordinates and to aggregate variables based on the spatial hierarchy of units. The object returned from the package can be used for thematic maps with the build-in functions provided in mapping or with other packages already available.
	"""
	
	homepage = "https://mappinguniverse.github.io/mapping/index.html"
	cran = "mapping" 

	version("1.4.1", md5="dd54afb9400f05a00c3cd11dc84e10c8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmap@3.3.3:", type=("build", "run"))
	depends_on("r-cartography@2.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-sf@1.0.0:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-leaflet@2.0.3:", type=("build", "run"))
	depends_on("r-tmaptools@2.0.2:", type=("build", "run"))
	depends_on("r-viridislite@0.3:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-htmltools@0.5:", type=("build", "run"))
	depends_on("r-leafpop@0.0.5:", type=("build", "run"))
	depends_on("r-leafsync@0.1:", type=("build", "run"))
	depends_on("r-mapview@2.7.8:", type=("build", "run"))
	depends_on("r-geojsonio@0.9.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-s2@1.0.6:", type=("build", "run"))
	depends_on("r-stringi@1.6.2:", type=("build", "run"))
