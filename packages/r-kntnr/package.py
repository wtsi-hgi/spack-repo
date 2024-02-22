# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKntnr(RPackage):
	"""R Client for 'kintone' API

	Retrieve data from 'kintone' (<https://www.kintone.com/>) via its API.
    'kintone' is an enterprise application platform.
	"""
	
	homepage = "https://yutannihilation.github.io/kntnr/"
	cran = "kntnr" 

	version("0.4.4", md5="d541b7b08dd12c289a76e4e6981cf660")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
