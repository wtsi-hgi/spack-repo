# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurl(RPackage):
	"""A Modern and Flexible Web Client for R.

	The curl() and curl_download() functions provide highly configurable
	drop-in replacements for base url() and download.file() with better
	performance, support for encryption (https, ftps), gzip compression,
	authentication, and other libcurl goodies. The core of the package
	implements a framework for performing fully customized requests where data
	can be processed either in memory, on disk, or streaming via the callback
	or connection interfaces. Some knowledge of libcurl is recommended; for a
	more-user-friendly web client see the 'httr' package which builds on this
	package with http specific tools and logic."""

	cran = "curl"

	license("MIT")

	version("5.2.1", md5="9380107ee0b1331ab730bd1e18b61c72")

	depends_on("r@3:", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
