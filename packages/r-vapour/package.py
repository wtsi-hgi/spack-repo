# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVapour(RPackage):
	"""Access to the 'Geospatial Data Abstraction Library' ('GDAL')

	Provides low-level access to 'GDAL' functionality.  
  'GDAL' is the 'Geospatial Data Abstraction Library' a translator for raster and vector geospatial data formats 
  that presents a single raster abstract data model and single vector abstract data model to the calling application 
  for all supported formats <https://gdal.org/>. This package is focussed on providing exactly and only what GDAL does, to enable
  developing further tools. 
	"""
	
	homepage = "https://github.com/hypertidy/vapour"
	cran = "vapour" 

	version("0.9.5", md5="11c458b43ae13473af3f4cfda94e4c69")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-nanoarrow", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("gdal@2.2.3:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
