# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartmap(RPackage):
	"""Smartly Create Maps from R Objects

	Preview spatial data as 'leaflet' maps with minimal
  effort. smartmap is optimized for interactive use and distinguishes itself 
  from similar packages because it does not need real spatial ('sp' or 'sf')
  objects an input; instead, it tries to automatically coerce everything that 
  looks like spatial data to sf objects or leaflet maps. It - for example -  
  supports direct mapping of: a vector containing a single coordinate pair,
  a two column matrix, a data.frame with longitude and latitude columns, or
  the path or URL to a (possibly compressed) 'shapefile'.
	"""
	
	cran = "smartmap" 

	version("0.1.1", md5="a570d8de081f5142cb64742ef5e37ee2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
