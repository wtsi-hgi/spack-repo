# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyredcap(RPackage):
	"""Helper Functions for Working with 'REDCap' Data

	
    Helper functions for processing 'REDCap' data in R. 'REDCap' is a 
    web-enabled application for building and managing surveys and databases 
    developed at Vanderbilt University.
	"""
	
	homepage = "https://raymondbalise.github.io/tidyREDCap/index.html"
	cran = "tidyREDCap" 

	version("1.1.1", md5="041326d88e0b552546eb7a2ffc39484f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-labelvector", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-redcapr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
