# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebmockr(RPackage):
	"""Stubbing and Setting Expectations on 'HTTP' Requests

	Stubbing and setting expectations on 'HTTP' requests.
    Includes tools for stubbing 'HTTP' requests, including expected
    request conditions and response conditions. Match on
    'HTTP' method, query parameters, request body, headers and
    more. Can be used for unit tests or outside of a testing 
    context.
	"""
	
	homepage = "https://github.com/ropensci/webmockr"
	cran = "webmockr" 

	version("0.9.0", md5="aabd7fb53dbb4b735ce4715fe976aaf2")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-r6@2.1.3:", type=("build", "run"))
	depends_on("r-urltools@1.6:", type=("build", "run"))
	depends_on("r-fauxpas", type=("build", "run"))
	depends_on("r-crul@0.7:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
