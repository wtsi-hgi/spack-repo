# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsrmr(RPackage):
	"""Wrapper for the 'OSRM' API

	Wrapper around the 'Open Source Routing Machine (OSRM)'
        API <http://project-osrm.org/>. 'osrmr' works with API versions
        4 and 5 and can handle servers that run locally as well as the
        'OSRM' webserver.
	"""
	
	cran = "osrmr" 

	version("0.1.36", md5="e7043c0acf480d7aa3ecdeb17dcd2771")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
