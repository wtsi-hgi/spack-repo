# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWalmartapi(RPackage):
	"""Walmart Open API Wrapper

	Provides API access to the Walmart Open API <https://developer.walmartlabs.com/>, 
    that contains data about stores, Value of the day and products which 
    includes names, sale prices, shipping rates and taxonomies.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/walmartAPI"
	cran = "walmartAPI" 

	version("0.1.5", md5="3fd79cd7afa5ec9cff2f029eeaf6439b")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
