# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhitebox(RPackage):
	"""'WhiteboxTools' R Frontend

	An R frontend for the 'WhiteboxTools' library, which is an advanced geospatial data analysis platform developed by Prof. John Lindsay at the University of Guelph's Geomorphometry and Hydrogeomatics Research Group. 'WhiteboxTools' can be used to perform common geographical information systems (GIS) analysis operations, such as cost-distance analysis, distance buffering, and raster reclassification. Remote sensing and image processing tasks include image enhancement (e.g. panchromatic sharpening, contrast adjustments), image mosaicing, numerous filtering operations, simple classification (k-means), and common image transformations. 'WhiteboxTools' also contains advanced tooling for spatial hydrological analysis (e.g. flow-accumulation, watershed delineation, stream network analysis, sink removal), terrain analysis (e.g. common terrain indices such as slope, curvatures, wetness index, hillshading; hypsometric analysis; multi-scale topographic position analysis), and LiDAR data processing. Suggested citation: Lindsay (2016) <doi:10.1016/j.cageo.2016.07.003>.
	"""
	
	homepage = "https://github.com/opengeos/whiteboxR"
	cran = "whitebox" 

	version("2.3.4", md5="ec1c97b9c2764b264347a32675e89f86")

	depends_on("r@3:", type=("build", "run"))
