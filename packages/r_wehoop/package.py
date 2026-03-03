# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWehoop(RPackage):
	"""Access Women's Basketball Play by Play Data

	A utility for working with women's basketball data. A scraping and aggregating interface for the WNBA Stats API <https://stats.wnba.com/> and ESPN's <https://www.espn.com> women's college basketball and WNBA statistics. It provides users with the capability to access the game play-by-plays, box scores, standings and results to analyze the data for themselves.
	"""
	
	homepage = "https://wehoop.sportsdataverse.org"
	cran = "wehoop" 

	version("2.0.0", md5="80a7943dd397ecf24fe3aca1978efe25")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-progressr@0.6:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-usethis@1.6:", type=("build", "run"))
