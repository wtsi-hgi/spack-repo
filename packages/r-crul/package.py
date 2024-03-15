# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrul(RPackage):
	"""HTTP Client.

	A simple HTTP client, with tools for making HTTP requests, and mocking HTTP
	requests. The package is built on R6, and takes inspiration from Ruby's
	'faraday' gem (<https://rubygems.org/gems/faraday>). The package name is a
	play on curl, the widely used command line tool for HTTP, and this package
	is built on top of the R package 'curl', an interface to 'libcurl'
	(<https://curl.haxx.se/libcurl>)."""

	cran = "crul"

	license("MIT")

	version("1.4.0", md5="b022130862a5b48886b3e0290181fc3a")

	depends_on("r-curl@3.3:", type=("build", "run"))
	depends_on("r-r6@2.2:", type=("build", "run"))
	depends_on("r-urltools@1.6:", type=("build", "run"))
	depends_on("r-httpcode@0.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
