# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartsheetr(RPackage):
	"""Access and Write 'Smartsheet' Data using the 'Smartsheet' API
2.0

	Interact with the 'Smartsheet' platform through the 'Smartsheet' 
  API 2.0. <https://smartsheet.redoc.ly/>. API is an acronym for
  application programming interface; the 'Smartsheet' API allows users to
  interact with 'Smartsheet' sheets directly within R. 
	"""
	
	cran = "smartsheetr" 

	version("0.1.0", md5="51e26703766c996f3c10914d0bdce2a1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
