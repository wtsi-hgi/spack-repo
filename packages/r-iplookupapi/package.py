# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIplookupapi(RPackage):
	"""Client for the 'iplookupapi.com' IP Lookup API

	An R client for the 'iplookupapi.com' IP Lookup API. The API requires registration of an API key. Basic features are free, some require a paid subscription. You can find the full API documentation at <https://iplookupapi.com/docs> .
	"""
	
	homepage = "https://iplookupapi.com"
	cran = "iplookupapi" 

	version("0.1.0", md5="9d1e8ffe4ea5e5c71612ac00b41d5f77")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
