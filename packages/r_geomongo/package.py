# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomongo(RPackage):
	"""Geospatial Queries Using 'PyMongo'

	Utilizes methods of the 'PyMongo' 'Python' library to initialize, insert and query 'GeoJson' data (see <https://github.com/mongodb/mongo-python-driver> for more information on 'PyMongo'). Furthermore, it allows the user to validate 'GeoJson' objects and to use the console for 'MongoDB' (bulk) commands. The 'reticulate' package provides the 'R' interface to 'Python' modules, classes and functions.
	"""
	
	homepage = "https://github.com/mlampros/GeoMongo"
	cran = "GeoMongo" 

	version("1.0.3", md5="933ae661c3764555c01b2ff51e6036a2")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-geojsonr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("mongodb@3.4.0:", type=("build", "link", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
