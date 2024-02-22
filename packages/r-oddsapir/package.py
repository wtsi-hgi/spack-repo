# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROddsapir(RPackage):
	"""Access Live Sports Odds from the Odds API

	A utility to quickly obtain clean and tidy sports
    odds from The Odds API <https://the-odds-api.com>.
	"""
	
	homepage = "https://oddsapiR.sportsdataverse.org/"
	cran = "oddsapiR" 

	version("0.0.3", md5="d5d9db1dcc893e05c33cb0c7953330b8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3.4.1:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr@0.5:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
