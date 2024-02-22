# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSorvi(RPackage):
	"""Functions for Finnish Open Data

	Misc support functions for rOpenGov and open data downloads.
	"""
	
	homepage = "https://github.com/ropengov/sorvi"
	cran = "sorvi" 

	version("0.8.21", md5="413047eb824df871a1bc0e8b23fbc37b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dlstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
