# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanscorer(RPackage):
	"""Score Redistricting Plans with 'PlanScore'

	Provides access to the 'PlanScore' Application Programming Interface 
    (<https://github.com/PlanScore/PlanScore/blob/main/API.md>) for scoring redistricting
    plans. Allows for upload of plans from block assignment files and shape files. 
    For shapes in memory, such as from 'sf' or 'redist', it processes them to save
    and upload. Includes tools for tidying responses and saving output from the 
    website.
	"""
	
	homepage = "http://christophertkenny.com/planscorer/"
	cran = "planscorer" 

	version("0.0.1", md5="0f8fe044615df9a8828e2fbc1b89b709")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
