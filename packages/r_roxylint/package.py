# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoxylint(RPackage):
	"""Lint 'roxygen2'-Generated Documentation

	Provides formatting linting to 'roxygen2' tags. Linters report
    'roxygen2' tags that do not conform to a standard style. These linters
    can be a helpful check for building more consistent documentation and 
    to provide reminders about best practices or checks for typos. Default 
    linting suites are provided for common style guides such as the one 
    followed by the 'tidyverse', though custom linters can be registered by 
    other packages or be custom-tailored to a specific package.
	"""
	
	homepage = "https://github.com/openpharma/roxylint"
	cran = "roxylint" 

	version("0.1.0", md5="510ea8f383c9aa3195acd49da27a2774")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
