# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHakaiapi(RPackage):
	"""Authenticated HTTP Request Client for the 'Hakai' API

	Initializes a class that obtains API credentials and provides
    a method to use those credentials to make GET requests to the 'Hakai'
    API server. Usage instructions are documented at
    <https://hakaiinstitute.github.io/hakai-api/>.
	"""
	
	homepage = "https://github.com/HakaiInstitute/hakai-api-client-r"
	cran = "hakaiApi" 

	version("1.0.2", md5="36d233c76d038a8219e29a635b60ad61")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
