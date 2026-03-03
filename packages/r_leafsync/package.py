# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafsync(RPackage):
	"""Small Multiples for Leaflet Web Maps

	Create small multiples of several leaflet web maps with (optional) 
    synchronised panning and zooming control. When syncing is enabled all maps 
    respond to mouse actions on one map. This allows side-by-side comparisons
    of different attributes of the same geometries. Syncing can be adjusted
    so that any combination of maps can be synchronised.
	"""
	
	homepage = "https://github.com/r-spatial/leafsync"
	cran = "leafsync" 

	version("0.1.0", md5="57e425815635415956b48ae1991a695e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-htmltools@0.3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-leaflet@2.0.1:", type=("build", "run"))
