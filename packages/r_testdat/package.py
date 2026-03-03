# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestdat(RPackage):
	"""Data Unit Testing for R

	Test your data! An extension of the 'testthat' unit testing
    framework with a family of functions and reporting tools for checking
    and validating data frames.
	"""
	
	homepage = "https://socialresearchcentre.github.io/testdat/"
	cran = "testdat" 

	version("0.4.2", md5="d77af8f8a810942ba73a1df478677fa0")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-testthat@2:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
