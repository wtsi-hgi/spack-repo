# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebsocket(RPackage):
	"""'WebSocket' Client Library

	Provides a 'WebSocket' client interface for R.
    'WebSocket' is a protocol for low-overhead real-time communication:
    <https://en.wikipedia.org/wiki/WebSocket>.
	"""
	
	cran = "websocket" 

	version("1.4.1", md5="4e9a99ca5f1d29209393c3569b1efaa4")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-asioheaders", type=("build", "run"))
	depends_on("openssl@1.0.2:", type=("build", "link", "run"))
