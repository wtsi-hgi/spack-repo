# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RVcr(RPackage):
	"""Record 'HTTP' Calls to Disk

	Record test suite 'HTTP' requests and replays them during
    future runs. A port of the Ruby gem of the same name
    (<https://github.com/vcr/vcr/>). Works by hooking into the 'webmockr'
    R package for matching 'HTTP' requests by various rules ('HTTP' method,
    'URL', query parameters, headers, body, etc.), and then caching
    real 'HTTP' responses on disk in 'cassettes'. Subsequent 'HTTP' requests
    matching any previous requests in the same 'cassette' use a cached
    'HTTP' response.
	"""
	
	homepage = "https://github.com/ropensci/vcr/"
	cran = "vcr" 

	version("1.2.2", md5="93aa22ac7dc2e88156ddfb92bfd20ee5")

	depends_on("r-crul@0.8.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-webmockr@0.8.0:", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
