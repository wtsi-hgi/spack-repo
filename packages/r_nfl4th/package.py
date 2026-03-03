# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNfl4th(RPackage):
	"""Functions to Calculate Optimal Fourth Down Decisions in the
National Football League

	A set of functions to estimate outcomes of fourth down
    plays in the National Football League and obtain fourth down plays
    from <https://www.nfl.com/> and <https://www.espn.com/>.
	"""
	
	homepage = "https://www.nfl4th.com/"
	cran = "nfl4th" 

	version("1.0.4", md5="01b26215fc17c8765d90ccff548d3959")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-backports@1.1.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nflfastr@4:", type=("build", "run"))
	depends_on("r-nflreadr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
