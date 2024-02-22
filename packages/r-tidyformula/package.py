# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyformula(RPackage):
	"""Build Formulas Using Tidy Selection Helpers

	Provides the function 'tidyformula()', which translates formulas containing 'tidyselect'-style selection helpers. It expands these helpers by evaluating 'dplyr::select()' with the relevant selection helper and a supplied data frame. The package contains methods for traversing abstract syntax trees from Wickham, Hadley (2019) <doi:10.1201/9781351201315>.
	"""
	
	cran = "tidyformula" 

	version("0.1.0", md5="6168ba093b9957334d0362f76576647f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
