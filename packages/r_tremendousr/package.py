# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTremendousr(RPackage):
	"""Easily Send Rewards and Incentives with 'Tremendous' from R

	A slightly-opinionated R interface for the 'Tremendous' API (<https://www.tremendous.com/>). 
    In addition to supporting GET and POST requests, 'tremendousr' has, dare I say, 
    tremendously intuitive functions for sending digital rewards and incentives directly from R.
	"""
	
	cran = "tremendousr" 

	version("1.0.0", md5="7114c4fd895c1a163442d6eadd002d83")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
