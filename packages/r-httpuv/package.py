# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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
	version("1.6.9", sha256="8d77f25b22fa7473b45007c2048e9a38d3792d59b2716e1fcdf9e99bd585d95d")
	version("1.6.6", sha256="41395fd324c5cb884d4f2a8060744758904119db22eeb312f2ea1e7ad7711293")
	version("1.6.5", sha256="f5f63629ca5e9d0e396a89982d95b5286726c0cb425166f35a3ad32a60a79156")
	version("1.6.15", md5="36b144ddfa37b5d0ed7f10d07a3b0c29")
	version("1.6.14", md5="ee8e55894d9e63e991dd28224da42b93")
	version("1.5.5", sha256="0be6c98927c7859d4bbfbbec8822c9f5e95352077d87640a76bc2ade07c83117")
	version("1.5.1", sha256="b5bb6b3b2f1a6d792568a70f3f357d6b3a35a5e26dd0c668c61a31f2ae8f5710")
	version("1.3.5", sha256="4336b993afccca2a194aca577b1975b89a35ac863423b18a11cdbb3f8470e4e9")
	version("1.3.3", sha256="bb37452ddc4d9381bee84cdf524582859af6a988e291debb71c8a2e120d02b2a")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
