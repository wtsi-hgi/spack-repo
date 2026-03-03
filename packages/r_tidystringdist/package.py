# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidystringdist(RPackage):
	"""String Distance Calculation with Tidy Data Principles

	Calculation of string distance following the tidy
    data principles. Built on top of the 'stringdist' package.
	"""
	
	cran = "tidystringdist" 

	version("0.1.4", md5="5dcd39a32155adac53bd3e66e4977f74")

	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
