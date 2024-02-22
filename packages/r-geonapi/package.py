# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeonapi(RPackage):
	"""'GeoNetwork' API R Interface

	Provides an R interface to the 'GeoNetwork' API (<https://geonetwork-opensource.org/#api>) allowing to upload and publish metadata in a 'GeoNetwork' web-application and expose it to OGC CSW.
	"""
	
	homepage = "https://github.com/eblondel/geonapi/wiki"
	cran = "geonapi" 

	version("0.7", md5="e4b1e116d68f3b84bc2a21d76af50d1d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-geometa", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
