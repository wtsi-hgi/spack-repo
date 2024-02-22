# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPocketapi(RPackage):
	"""Wrapper Around the 'Pocket' API

	Functions that interface with the 'Pocket' API (<https://getpocket.com/developer/>). Allows the user to get, add, and modify items in their own 'Pocket' account.
	"""
	
	homepage = "https://github.com/CorrelAid/pocketapi/"
	cran = "pocketapi" 

	version("0.1", md5="f86cfa229c78de8e5317b7184024e333")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
