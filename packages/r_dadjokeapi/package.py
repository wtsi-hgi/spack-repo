# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDadjokeapi(RPackage):
	"""Return a Random Dad Joke

	What is funnier than a dad joke?  A dad joke in R!  This package 
    utilizes the API for <https://icanhazdadjoke.com> and returns dad jokes from
    several API endpoints.
	"""
	
	homepage = "https://github.com/jhollist/dadjokeapi/"
	cran = "dadjokeapi" 

	version("1.0.2", md5="cd2e06087e15be7e3e230d45f3cdbb71")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
