# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNflseedr(RPackage):
	"""Functions to Efficiently Simulate and Evaluate NFL Seasons

	A set of functions to simulate National Football League
    seasons including the sophisticated tie-breaking procedures.
	"""
	
	homepage = "https://nflseedr.com"
	cran = "nflseedR" 

	version("1.2.0", md5="3a04558152403f14031d142994ee88de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nflreadr@1.1.3:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
