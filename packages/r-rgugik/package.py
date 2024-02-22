# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgugik(RPackage):
	"""Search and Retrieve Spatial Data from 'GUGiK'

	Automatic open data acquisition from resources of Polish Head Office
    of Geodesy and Cartography ('Główny Urząd Geodezji i Kartografii')
    (<https://www.gov.pl/web/gugik>).
    Available datasets include various types of numeric, raster and vector data,
    such as orthophotomaps, digital elevation models (digital terrain models,
    digital surface model, point clouds), state register of borders, spatial
    databases, geometries of cadastral parcels, 3D models of buildings, and more.
    It is also possible to geocode addresses or objects using the geocodePL_get()
    function.
	"""
	
	homepage = "https://kadyb.github.io/rgugik/"
	cran = "rgugik" 

	version("0.4.0", md5="9bd1a51b2e44bbeea56c7d4fce9d0261")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
