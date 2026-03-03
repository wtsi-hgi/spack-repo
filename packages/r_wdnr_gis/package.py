# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWdnrGis(RPackage):
	"""Pull Spatial Layers from 'WDNR ArcGIS REST API'

	Functions for finding and pulling data from the
  'Wisconsin Department of Natural Resources ArcGIS REST APIs'
  <https://dnrmaps.wi.gov/arcgis/rest/services> and 
  <https://dnrmaps.wi.gov/arcgis2/rest/services>.
	"""
	
	cran = "wdnr.gis" 

	version("0.1.5", md5="220e98acfb670e8ff42e0fd28190b3a8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-arcpullr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
