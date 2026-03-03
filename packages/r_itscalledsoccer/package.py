# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItscalledsoccer(RPackage):
	"""American Soccer Analysis API Client

	Provides a wrapper around the same API <https://app.americansocceranalysis.com/api/v1/__docs__/>
    that powers the American Soccer Analysis app.
	"""
	
	homepage = "https://github.com/American-Soccer-Analysis/itscalledsoccer-r"
	cran = "itscalledsoccer" 

	version("0.2.4", md5="4ff662dc5d8e1fbe6dddf296fa7071b7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httpcache@1.2:", type=("build", "run"))
	depends_on("r-glue@1.4.1:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-r6@2.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-stringi@1.5.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
