# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExampletestr(RPackage):
	"""Help for Writing Unit Tests Based on Function Examples

	Take the examples written in your documentation of functions
    and use them to create shells (skeletons which must be manually
    completed by the user) of test files to be tested with the 'testthat'
    package. Sort of like python 'doctests' for R.
	"""
	
	homepage = "https://rorynolan.github.io/exampletestr/"
	cran = "exampletestr" 

	version("1.7.1", md5="28d0d90a53f50e747763b56177bdee00")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-fs@1.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-rstudioapi@0.4:", type=("build", "run"))
	depends_on("r-strex@1.4.2:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-styler@1.2:", type=("build", "run"))
	depends_on("r-usethis@2:", type=("build", "run"))
	depends_on("r-withr@2.1:", type=("build", "run"))
