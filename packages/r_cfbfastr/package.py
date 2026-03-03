# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfbfastr(RPackage):
	"""Access College Football Play by Play Data

	A utility to quickly obtain clean and tidy college football
    data. Serves as a wrapper around the
    <https://collegefootballdata.com/> API and provides functions to
    access live play by play and box score data from ESPN
    <https://www.espn.com> when available. It provides users the
    capability to access a plethora of endpoints, and supplement that data
    with additional information (Expected Points Added/Win Probability
    added).
	"""
	
	homepage = "https://cfbfastR.sportsdataverse.org/"
	cran = "cfbfastR" 

	version("1.9.0", md5="29e15735e17ab52d6a4226d21b375c63")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mgcv@1.8.33:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-progressr@0.6:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
