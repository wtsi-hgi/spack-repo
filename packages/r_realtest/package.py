# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRealtest(RPackage):
	"""Where Expectations Meet Reality: Realistic Unit Testing

	
    A framework for unit testing for realistic minimalists,
    where we distinguish between expected, acceptable, current, fallback,
    ideal, or regressive behaviour. It can also be used for monitoring
    third-party software projects for changes.
	"""
	
	homepage = "https://realtest.gagolewski.com"
	cran = "realtest" 

	version("0.2.3", md5="8f12bdb7b0f31943d36ab75329c8a923")

	depends_on("r@4:", type=("build", "run"))
