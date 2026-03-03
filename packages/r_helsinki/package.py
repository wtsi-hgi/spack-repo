# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHelsinki(RPackage):
	"""R Tools for Helsinki Open Data

	Tools for accessing various open data APIs in the Helsinki
    region in Finland. Current data sources include the Service Map API,
    Linked Events API, and Helsinki Region Infoshare statistics API.
	"""
	
	homepage = "http://ropengov.github.io/helsinki/"
	cran = "helsinki" 

	version("1.0.6", md5="79723405d193a8e7756859cbb62597c8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
