# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartialised(RPackage):
	"""Partialised Functions

	Provides a 'partialised' class that extends the partialising 
    function of 'purrr' by making it easier to change the arguments. This is 
    similar to the function-like object in 'Julia' 
    (<https://docs.julialang.org/en/v1/manual/methods/#Function-like-objects>).
	"""
	
	homepage = "https://github.com/UchidaMizuki/partialised"
	cran = "partialised" 

	version("0.1.1", md5="7912c3b78384a64b8358436577f459ff")

	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
