# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactsetAnalyticsapiEngines(RPackage):
	"""'FactSet' Engines API Client

	Allow clients to fetch 'analytics' through API for Portfolio 
    'Analytics'('PA'), Style Performance Risk('SPAR') and 'Vault' products of 
    'FactSet'. Visit 
    <https://github.com/factset/analyticsapi-engines-r-sdk/tree/master/Engines>
    for more information on the usage of package. Visit 
    <https://developer.factset.com/> for more information on products.
	"""
	
	homepage = "https://github.com/factset/analyticsapi-engines-r-sdk"
	cran = "factset.analyticsapi.engines" 

	version("3.0.1", md5="822e8b56fd841e70a7aa365eefca737d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
