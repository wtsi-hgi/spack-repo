# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttpcache(RPackage):
	"""Query Cache for HTTP Clients

	In order to improve performance for HTTP API clients, 'httpcache'
    provides simple tools for caching and invalidating cache. It includes the
    HTTP verb functions GET, PUT, PATCH, POST, and DELETE, which are drop-in
    replacements for those in the 'httr' package. These functions are cache-aware
    and provide default settings for cache invalidation suitable for RESTful
    APIs; the package also enables custom cache-management strategies.
    Finally, 'httpcache' includes a basic logging framework to facilitate the
    measurement of HTTP request time and cache performance.
	"""
	
	homepage = "https://enpiar.com/r/httpcache/"
	cran = "httpcache" 

	version("1.2.0", md5="ce9ae37f774d29bea0548fd1c022fc23")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
