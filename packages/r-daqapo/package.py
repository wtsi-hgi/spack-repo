# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaqapo(RPackage):
	"""Data Quality Assessment for Process-Oriented Data

	Provides a variety of methods to identify data quality issues in process-oriented data, which are useful to verify data quality in a process mining context. Builds on the class for activity logs implemented in the package 'bupaR'. Methods to identify data quality issues either consider each activity log entry independently (e.g. missing values, activity duration outliers,...), or focus on the relation amongst several activity log entries (e.g. batch registrations, violations of the expected activity order,...).
	"""
	
	homepage = "https://github.com/bupaverse/daqapo/"
	cran = "daqapo" 

	version("0.3.2", md5="b94983bfbfff1f1e1a1cb8ecc8d5cb74")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xesreadr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-bupar@0.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-edear", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
