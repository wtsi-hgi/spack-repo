# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElevatr(RPackage):
	"""Access Elevation Data from Various APIs

	Several web services are available that provide access to elevation
             data. This package provides access to many of those services and 
             returns elevation data either as an 'sf' simple features object 
             from point elevation services or as a 'raster' object from raster 
             elevation services. In future versions, 'elevatr' will drop 
             support for 'raster' and will instead return 'terra' objects. 
             Currently, the package supports access to the Amazon Web Services 
             Terrain Tiles <https://registry.opendata.aws/terrain-tiles/>, 
             the Open Topography Global Datasets 
             API <https://opentopography.org/developers/>, and the USGS 
             Elevation Point Query Service <https://apps.nationalmap.gov/epqs/>.
	"""
	
	homepage = "https://github.com/jhollist/elevatr/"
	cran = "elevatr" 

	version("0.99.0", md5="ac057860e9a709c63fb042b3f2c879ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-slippymath", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
