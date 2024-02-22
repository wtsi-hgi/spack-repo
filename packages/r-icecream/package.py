# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcecream(RPackage):
	"""Print Debugging Made Sweeter

	Provides user-friendly and configurable print debugging via a
    single function, ic(). Wrap an expression in ic() to print the
    expression, its value and (where available) its source location.
    Debugging output can be toggled globally without modifying code.
	"""
	
	homepage = "https://www.lewinfox.com/icecream/"
	cran = "icecream" 

	version("0.2.2", md5="59ae2e173f05a8c37d15d11ff08bc111")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pillar@1.6.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
