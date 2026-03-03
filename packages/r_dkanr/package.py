# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDkanr(RPackage):
	"""Client for the 'DKAN' API

	Provides functions to facilitate access to the 'DKAN' API (<https://dkan.readthedocs.io/en/latest/apis/index.html>), including the 'DKAN' REST API (metadata), and the 'DKAN' datastore API (data). Includes functions to list, create, retrieve, update, and delete datasets and resources nodes. It also includes functions to search and retrieve data from the 'DKAN' datastore. 
	"""
	
	cran = "dkanr" 

	version("0.1.3", md5="85a25b69f9b42891b19df73a129372e8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
