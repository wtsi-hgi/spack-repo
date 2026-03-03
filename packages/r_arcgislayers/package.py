# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcgislayers(RPackage):
	"""An Interface to ArcGIS Data Services

	Enables users of 'ArcGIS Enterprise', 'ArcGIS Online', or
    'ArcGIS Platform' to read, write, publish, or manage vector and raster
    data via ArcGIS location services REST API endpoints
    <https://developers.arcgis.com/rest/>.
	"""
	
	cran = "arcgislayers" 

	version("0.2.0", md5="4eb1cc4407011e4e8b7378c91b1b4954")

	depends_on("r-arcgisutils@0.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-jsonify", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcppsimdjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
