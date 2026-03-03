# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstrio(RPackage):
	"""Interface for 'MicroStrategy' REST API

	Interface for creating data sets and extracting data through the
    'MicroStrategy' REST API. Access the demo API at
    <https://demo.microstrategy.com/MicroStrategyLibrary/api-docs/index.html>.
	"""
	
	cran = "mstrio" 

	version("11.3.5.101", md5="fceab41c3420e97bdb183d511063b198")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-openssl@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-vctrs@0.3.8:", type=("build", "run"))
