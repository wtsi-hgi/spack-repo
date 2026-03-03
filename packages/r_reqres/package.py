# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReqres(RPackage):
	"""Powerful Classes for HTTP Requests and Responses

	In order to facilitate parsing of http requests and creating 
    appropriate responses this package provides two classes to handle a lot of
    the housekeeping involved in working with http exchanges. The infrastructure
    builds upon the 'rook' specification and is thus well suited to be combined
    with 'httpuv' based web servers.
	"""
	
	homepage = "https://reqres.data-imaginist.com"
	cran = "reqres" 

	version("0.2.5", md5="f8e6eeb1c5bf0ddb4a9f58436c1e1296")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-brotli", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-webutils", type=("build", "run"))
