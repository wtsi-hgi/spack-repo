# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpostgis(RPackage):
	"""R Interface to a 'PostGIS' Database

	Provides an interface between R and 'PostGIS'-enabled
    'PostgreSQL' databases to transparently transfer spatial
    data. Both vector (points, lines, polygons) and raster data are
    supported in read and write modes. Also provides convenience
    functions to execute common procedures in 'PostgreSQL/PostGIS'.
	"""
	
	homepage = "https://cidree.github.io/rpostgis/"
	cran = "rpostgis" 

	version("1.5.1", md5="9408c17b0eab54d8cca1ba2d2a3f8ae1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-dbi@0.5:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra@1.6.7:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("postgresql+client_only", type=("build", "link", "run"))
