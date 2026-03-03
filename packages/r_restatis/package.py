# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestatis(RPackage):
	"""Web API Client for the German Federal Statistical Office
Database

	A 'RESTful' API wrapper for accessing the 'GENESIS' database
    of the German Federal Statistical Office (Destatis)
    <https://www-genesis.destatis.de/>. Also supports data search
    functions, credential management, result caching, and handling remote
    background jobs for large datasets.
	"""
	
	homepage = "https://correlaid.github.io/restatis/"
	cran = "restatis" 

	version("0.1.0", md5="a56259cb22d829a7c832d2864bad0f1d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
