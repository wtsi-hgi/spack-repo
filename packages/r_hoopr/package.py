# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHoopr(RPackage):
	"""Access Men's Basketball Play by Play Data

	A utility to quickly obtain clean and tidy men's
    basketball play by play data. Provides functions to access
    live play by play and box score data from ESPN<https://www.espn.com> with shot locations
    when available. It is also a full NBA Stats API<https://www.nba.com/stats/> wrapper.
    It is also a scraping and aggregating interface for Ken Pomeroy's 
    men's college basketball statistics website<https://kenpom.com>. It provides users with an
    active subscription the capability to scrape the website tables and
    analyze the data for themselves.
	"""
	
	homepage = "https://github.com/sportsdataverse/hoopR"
	cran = "hoopR" 

	version("2.1.0", md5="55b8370a23a29b6c1c304c1b92a799f6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@1.1:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr@0.5:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progressr@0.6:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-usethis@1.6:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
