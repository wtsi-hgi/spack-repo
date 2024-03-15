# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtrrr(RPackage):
	"""Wrapper for the 'AT' Protocol Behind 'Bluesky'

	Wraps the 'AT' Protocol (Authenticated Transfer Protocol) behind 
    'Bluesky' <https://bsky.social>. Functions can be used for, among others, 
    retrieving posts and followers from the network or posting content.
	"""
	
	homepage = "https://jbgruber.github.io/atrrr/"
	cran = "atrrr" 

	version("0.0.3", md5="bf02d61096aa96e7a762e2b6bc979241")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
