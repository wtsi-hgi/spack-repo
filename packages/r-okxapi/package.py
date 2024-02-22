# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROkxapi(RPackage):
	"""An Unofficial Wrapper for 'okx exchange v5' API

	An unofficial wrapper for 'okx exchange v5' API <https://www.okx.com/docs-v5/en/>, including 'REST' API and 'WebSocket' API.
	"""
	
	cran = "okxAPI" 

	version("0.1.1", md5="04051020f59f59d140018461ff536b35")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-websocket", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
