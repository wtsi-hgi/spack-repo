# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttpuv(RPackage):
	"""HTTP and WebSocket Server Library.

	Provides low-level socket and protocol support for handling HTTP and
	WebSocket requests directly from within R. It is primarily intended as a
	building block for other packages, rather than making it particularly easy
	to create complete web applications using httpuv alone. httpuv is built on
	top of the libuv and http-parser C libraries, both of which were developed
	by Joyent, Inc. (See LICENSE file for libuv and http-parser license
	information.)"""

	cran = "httpuv"

	license("GPL-2.0-or-later OR custom")

	version("1.6.14", md5="ee8e55894d9e63e991dd28224da42b93")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
