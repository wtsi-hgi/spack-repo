# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazamacoreutils(RPackage):
	"""Utility Functions for Production R Code

	A suite of utility functions providing functionality commonly
    needed for production level projects such as logging, error handling,
    cache management and date-time parsing. Functions for date-time parsing and 
    formatting require that time zones be specified explicitly, avoiding a common 
    source of error when working with environmental time series.
	"""
	
	homepage = "https://github.com/MazamaScience/MazamaCoreUtils"
	cran = "MazamaCoreUtils" 

	version("0.5.2", md5="70001f3fab3c71ca8f004d8e5075f72f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-geohashtools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
