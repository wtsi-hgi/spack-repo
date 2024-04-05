# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosapi(RPackage):
	"""GeoServer REST API R Interface

	Provides an R interface to the GeoServer REST API, allowing to upload 
 and publish data in a GeoServer web-application and expose data to OGC Web-Services. 
 The package currently supports all CRUD (Create,Read,Update,Delete) operations
 on GeoServer workspaces, namespaces, datastores (stores of vector data), featuretypes,
 layers, styles, as well as vector data upload operations. For more information about 
 the GeoServer REST API, see <https://docs.geoserver.org/stable/en/user/rest/>.
	"""
	
	homepage = "https://github.com/eblondel/geosapi"
	cran = "geosapi" 

	version("0.7-1", md5="179ca222c6218299462cdb3b7a8b8b8e")
	version("0.6-7", md5="2f94a787f23f63b8c193b5307315bf13")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
