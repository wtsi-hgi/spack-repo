# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBroomHelpers(RPackage):
	"""Helpers for Model Coefficients Tibbles

	Provides suite of functions to work with regression model
    'broom::tidy()' tibbles.  The suite includes functions to group
    regression model terms by variable, insert reference and header rows
    for categorical variables, add variable labels, and more.
	"""
	
	homepage = "https://larmarange.github.io/broom.helpers/"
	cran = "broom.helpers" 

	version("1.14.0", md5="1f788779512992613da0c5619f0e0d33")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-broom@0.8:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.0.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
