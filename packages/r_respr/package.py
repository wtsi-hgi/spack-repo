# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRespr(RPackage):
	"""Import, Process, Analyse, and Calculate Rates from Respirometry
Data

	Provides a structural, reproducible workflow for the
    processing and analysis of respirometry data. It contains analytical
    functions and utilities for working with oxygen time-series to determine
    respiration or oxygen production rates, and to make it easier to report and
    share analyses. See Harianto et al. 2019 <doi:10.1111/2041-210X.13162>.
	"""
	
	homepage = "https://github.com/januarharianto/respr"
	cran = "respR" 

	version("2.3.2", md5="074482a729a9aef26275d69aaca1aeb8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-marelac", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-roll", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
