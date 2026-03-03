# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeech(RPackage):
	"""Legislative Speeches

	Converts the floor speeches of Uruguayan legislators, extracted from the 
    parliamentary minutes, to tidy data.frame where each observation is the intervention of a single legislator.
	"""
	
	homepage = "https://github.com/Nicolas-Schmidt/speech"
	cran = "speech" 

	version("0.1.5", md5="d58e630b23a3cef0910d3a266dbdd873")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
