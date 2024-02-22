# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRequest(RPackage):
	"""High Level 'HTTP' Client

	High level and easy 'HTTP' client for 'R'. Provides functions for
    building 'HTTP' queries, including query parameters, body requests, headers,
    authentication, and more.
	"""
	
	homepage = "https://github.com/sckott/request"
	cran = "request" 

	version("0.1.0", md5="e764476fb60af87e5569e51ae72882d3")

	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-curl@0.9.4:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-lazyeval@0.1.10:", type=("build", "run"))
	depends_on("r-whisker@0.3.2:", type=("build", "run"))
	depends_on("r-r6@2.1.1:", type=("build", "run"))
