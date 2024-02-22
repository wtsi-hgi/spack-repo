# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenstreetmap(RPackage):
	"""Access to Open Street Map Raster Images

	Accesses high resolution raster maps using the OpenStreetMap
    protocol. Dozens of road, satellite, and topographic map servers are directly
    supported, including Apple, Mapnik, Bing, and stamen. Additionally raster maps
    may be constructed using custom tile servers.  Maps can be
    plotted using either base graphics, or ggplot2. This package is not affiliated
    with the OpenStreetMap.org mapping project.
	"""
	
	homepage = "https://github.com/ifellows/ROSM"
	cran = "OpenStreetMap" 

	version("0.4.0", md5="702fc304faafb130fdb66201cc74c2b8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2@0.9:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
