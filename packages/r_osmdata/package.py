# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsmdata(RPackage):
	"""Import 'OpenStreetMap' Data as Simple Features or Spatial
Objects

	Download and import of 'OpenStreetMap' ('OSM') data as 'sf'
    or 'sp' objects.  'OSM' data are extracted from the 'Overpass' web
    server (<https://overpass-api.de/>) and processed with very fast 'C++'
    routines for return to 'R'.
	"""
	
	homepage = "https://docs.ropensci.org/osmdata/"
	cran = "osmdata" 

	version("0.2.5", md5="7694d9235340a4a525125eefadc1dc1f")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reproj", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
