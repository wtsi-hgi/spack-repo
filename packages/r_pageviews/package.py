# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPageviews(RPackage):
	"""An API Client for Wikimedia Traffic Data

	Pageview data from the 'Wikimedia' sites, such as
    'Wikipedia' <https://www.wikipedia.org/>, from entire projects to per-article
    levels of granularity, through the new RESTful API and data source <https://wikimedia.org/api/rest_v1/?doc>.
	"""
	
	homepage = "https://github.com/ironholds/pageviews"
	cran = "pageviews" 

	version("0.6.0", md5="c5b79ba951bc2af19276c6a8d33283d2")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
