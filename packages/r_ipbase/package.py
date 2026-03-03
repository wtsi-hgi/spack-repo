# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpbase(RPackage):
	"""Client for the 'ipbase.com' IP Geolocation API

	An R client for the 'ipbase.com' IP Geolocation API. The API requires registration of an API key. Basic features are free, some require a paid subscription. You can find the full API documentation at <https://ipbase.com/docs> .
	"""
	
	homepage = "https://ipbase.com"
	cran = "ipbase" 

	version("0.1.1", md5="06b314d3eaa2e054f95f322db3b2b636")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
