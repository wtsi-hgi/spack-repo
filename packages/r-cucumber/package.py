# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCucumber(RPackage):
	"""Behavior-Driven Development for R

	Write executable specifications in a natural language that describes how your code should behave.
    Write specifications in feature files using 'Gherkin' language and execute them using functions implemented in R.
    Use them as an extension to your 'testthat' tests to provide a high level description of how your code works.
	"""
	
	homepage = "https://github.com/jakubsob/cucumber"
	cran = "cucumber" 

	version("1.0.0", md5="fed8927cb73ef535c5634eb4583955f3")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
