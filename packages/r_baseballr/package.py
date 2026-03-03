# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaseballr(RPackage):
	"""Acquiring and Analyzing Baseball Data

	Provides numerous utilities for acquiring and analyzing
    baseball data from online sources such as 'Baseball Reference' <https://www.baseball-reference.com/>,
    'FanGraphs' <https://www.fangraphs.com/>, and the 'MLB Stats' API <https://www.mlb.com/>.
	"""
	
	homepage = "https://billpetti.github.io/baseballr/"
	cran = "baseballr" 

	version("1.6.0", md5="e193e0995a3dcac4f452241844028642")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3.4.1:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr@0.5:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
