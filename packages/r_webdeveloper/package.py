# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebdeveloper(RPackage):
	"""Functions for Web Development

	Organizational framework for web development in R including functions to  
    serve static and dynamic content via HTTP methods, includes the html5 package to
    create HTML pages, and offers other utility functions for common tasks related 
    to web development.
	"""
	
	cran = "webdeveloper" 

	version("1.0.5", md5="8200ceaf08d9c6be4d28bfc6b4d7321d")

	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-html5@1:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
