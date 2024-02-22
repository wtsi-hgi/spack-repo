# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFiery(RPackage):
	"""A Lightweight and Flexible Web Framework

	A very flexible framework for building server side logic in
    R. The framework is unopinionated when it comes to how HTTP requests
    and WebSocket messages are handled and supports all levels of app
    complexity; from serving static content to full-blown dynamic
    web-apps. Fiery does not hold your hand as much as e.g. the shiny
    package does, but instead sets you free to create your web app the way
    you want.
	"""
	
	homepage = "https://fiery.data-imaginist.com"
	cran = "fiery" 

	version("1.2.1", md5="f65451d467668b135fb2153e80f2293b")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reqres", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
