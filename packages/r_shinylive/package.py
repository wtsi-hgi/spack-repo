# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinylive(RPackage):
	"""Run 'shiny' Applications in the Browser

	Exporting 'shiny' applications with 'shinylive' allows you to run them entirely in a web browser, without the need for a separate R server. The traditional way of deploying 'shiny' applications involves in a separate server and client: the server runs R and 'shiny', and clients connect via the web browser. When an application is deployed with 'shinylive', R and 'shiny' run in the web browser (via 'webR'): the browser is effectively both the client and server for the application. This allows for your 'shiny' application exported by 'shinylive' to be hosted by a static web server.
	"""
	
	homepage = "https://posit-dev.github.io/r-shinylive/"
	cran = "shinylive" 

	version("0.1.1", md5="ab062b3cba5c7a552373c59b7d624fbc")

	depends_on("r-archive", type=("build", "run"))
	depends_on("r-brio", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
