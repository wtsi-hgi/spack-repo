# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoutr(RPackage):
	"""A Simple Router for HTTP and WebSocket Requests

	In order to make sure that web request ends up in the correct 
    handler function a router is often used. 'routr' is a package implementing a
    simple but powerful routing functionality for R based servers. It is a fully
    functional 'fiery' plugin, but can also be used with other 'httpuv' based
    servers.
	"""
	
	homepage = "https://routr.data-imaginist.com"
	cran = "routr" 

	version("0.4.1", md5="b543d923c870f3c13cf6646312935897")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-reqres", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
