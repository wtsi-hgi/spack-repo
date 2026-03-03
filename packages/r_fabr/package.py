# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabr(RPackage):
	"""Wrapper Functions Collection Used in Data Pipelines

	The goal of this package is to provide wrapper functions in the 
    data cleaning and cleansing processes. These function helps in messages and 
    interaction with the user, keep track of information in pipelines, help in 
    the wrangling, munging, assessment and visualization of data frame-like 
    material.
	"""
	
	homepage = "https://github.com/GuiFabre/fabR"
	cran = "fabR" 

	version("2.0.1", md5="9d1673397d249ae4702e23445a893cef")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
