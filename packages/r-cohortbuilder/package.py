# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohortbuilder(RPackage):
	"""Data Source Agnostic Filtering Tools

	Common API for filtering data stored in different data models.
    Provides multiple filter types and reproducible R code.
    Works standalone or with 'shinyCohortBuilder' as the GUI for interactive Shiny apps.
	"""
	
	homepage = "https://github.com/r-world-devs/cohortBuilder/"
	cran = "cohortBuilder" 

	version("0.2.0", md5="2eba5cfd48b0290bfed05e70051ed70c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
