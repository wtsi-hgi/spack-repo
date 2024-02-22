# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUstfd(RPackage):
	"""API Client for US Treasury Fiscal Data

	Make requests from the US Treasury Fiscal Data API endpoints.
	"""
	
	homepage = "https://github.com/groditi/ustfd"
	cran = "ustfd" 

	version("0.4.4", md5="153a0668dbaaca4941395754fa92fd58")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-snakecase@0.11:", type=("build", "run"))
