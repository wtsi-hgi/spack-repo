# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastrhockey(RPackage):
	"""Functions to Access Premier Hockey Federation and National
Hockey League Play by Play Data

	A utility to scrape and load play-by-play data
    and statistics from the Premier Hockey Federation (PHF) <https://www.premierhockeyfederation.com/>, formerly
    known as the National Women's Hockey League (NWHL). Additionally, allows access to the National Hockey League's
    stats API <https://www.nhl.com/>.
	"""
	
	homepage = "https://fastRhockey.sportsdataverse.org/"
	cran = "fastRhockey" 

	version("0.4.0", md5="32600da2c2166f933aaeca5a599ac033")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progressr@0.6:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
