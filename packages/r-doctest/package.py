# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoctest(RPackage):
	"""Generate Tests from Examples Using 'roxygen' and 'testthat'

	Creates 'testthat' tests from 'roxygen' examples using simple tags.
	"""
	
	homepage = "https://hughjonesd.github.io/doctest/"
	cran = "doctest" 

	version("0.3.0", md5="62e7fbd7a94a1d0305dae5b46c8942b4")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
