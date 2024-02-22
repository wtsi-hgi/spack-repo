# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRttwebclient(RPackage):
	"""Web Client to 'TickTrader'

	R Web Client to 'TickTrader' platform. Provides you access to 'TickTrader' platform through Web API <https://ttlivewebapi.fxopen.net:8443/api/doc/index>.
	"""
	
	cran = "RTTWebClient" 

	version("0.1.3", md5="7a3a559cb8d1e603c3b9ae4b3ee80637")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
