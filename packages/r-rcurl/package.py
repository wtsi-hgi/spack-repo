# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcurl(RPackage):
	"""General Network (HTTP/FTP/...) Client Interface for R.

	A wrapper for 'libcurl' <http://curl.haxx.se/libcurl/> Provides functions
	to allow one to compose general HTTP requests and provides convenient
	functions to fetch URIs, get & post forms, etc. and process the results
	returned by the Web server. This provides a great deal of control over the
	HTTP/FTP/... connection and the form of the request while providing a
	higher-level interface than is available just using R socket connections.
	Additionally, the underlying implementation is robust and extensive,
	supporting FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS, telnet, dict,
	ldap, and also supports cookies, redirects, authentication, etc."""

	cran = "RCurl"

	version("1.98-1.14", md5="db488a574c244647e793082ede268cc1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
