# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeojsonio(RPackage):
	"""Convert Data from and to 'GeoJSON' or 'TopoJSON'

	Convert data to 'GeoJSON' or 'TopoJSON' from various R
    classes, including vectors, lists, data frames, shape files, and
    spatial classes.  'geojsonio' does not aim to replace packages like
    'sp', 'rgdal', 'rgeos', but rather aims to be a high level client to
    simplify conversions of data from and to 'GeoJSON' and 'TopoJSON'.
	"""
	
	homepage = "https://github.com/ropensci/geojsonio"
	cran = "geojsonio" 

	version("0.11.3", md5="e316958f9bd5390bda02210e5f47b10c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-geojson@0.2:", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-jqr", type=("build", "run"))
	depends_on("r-jsonlite@0.9.21:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr@0.2.2:", type=("build", "run"))
	depends_on("r-sf@0.6:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
