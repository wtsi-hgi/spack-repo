# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNofrills(RPackage):
	"""Low-Cost Anonymous Functions

	Provides a compact variation of the usual syntax of function
  declaration, in order to support tidyverse-style quasiquotation of a
  function's arguments and body.
	"""
	
	homepage = "https://github.com/egnha/nofrills"
	cran = "nofrills" 

	version("0.3.2", md5="5ebb619265df3b5d9e7aff47afe3ede6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
