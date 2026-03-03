# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCkanr(RPackage):
	"""Client for the Comprehensive Knowledge Archive Network ('CKAN')
API

	Client for 'CKAN' API (<https://ckan.org/>). Includes interface
    to 'CKAN' 'APIs' for search, list, show for packages, organizations, and
    resources. In addition, provides an interface to the 'datastore' API.
	"""
	
	homepage = "https://docs.ropensci.org/ckanr/"
	cran = "ckanr" 

	version("0.7.0", md5="d00638659eac5197c04e35c1a9cdf613")

	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-jsonlite@0.9.17:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
