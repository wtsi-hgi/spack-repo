# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfars(RPackage):
	"""Download and Analyze Crash Data

	Download crash data from the National Highway Traffic Safety Administration and prepare it for research.
	"""
	
	homepage = "https://github.com/s87jackson/rfars"
	cran = "rfars" 

	version("1.1.0", md5="7006d009506dd3e25cdbeb556a74497c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sas7bdat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
