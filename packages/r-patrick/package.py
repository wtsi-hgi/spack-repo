# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatrick(RPackage):
	"""Parameterized Unit Testing

	This is an extension of the 'testthat' package that
    lets you add parameters to your unit tests. Parameterized unit tests
    are often easier to read and more reliable, since they follow the DNRY
    (do not repeat yourself) rule.
	"""
	
	homepage = "https://github.com/google/patrick"
	cran = "patrick" 

	version("0.2.0", md5="e3e96321a6ebb8b6b18fa4a302085620")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
