# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmapshaper(RPackage):
	"""Client for 'mapshaper' for 'Geospatial' Operations

	Edit and simplify 'geojson', 'Spatial', and 'sf'
    objects.  This is wrapper around the 'mapshaper' 'JavaScript' library
    by Matthew Bloch <https://github.com/mbloch/mapshaper/> to perform
    topologically-aware polygon simplification, as well as other
    operations such as clipping, erasing, dissolving, and converting
    'multi-part' to 'single-part' geometries.
	"""
	
	homepage = "https://github.com/ateucher/rmapshaper"
	cran = "rmapshaper" 

	version("0.5.0", md5="bb4e6a91994daa702c157939b400dd28")

	depends_on("r-geojsonsf@2.0.2:", type=("build", "run"))
	depends_on("r-jsonify@1.2:", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-sp@1.4.0:", type=("build", "run"))
	depends_on("r-v8@4:", type=("build", "run"))
