# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogrx(RPackage):
	"""A Logging Utility Focus on Clinical Trial Programming Workflows

	A utility to facilitate the logging and review of R programs in clinical trial programming workflows.
	"""
	
	homepage = "https://github.com/pharmaverse/logrx"
	cran = "logrx" 

	version("0.3.0", md5="7e4993350fa0418cdc4b51d1bf93fce8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sessioninfo@1.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
