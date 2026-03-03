# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCookiemonster(RPackage):
	"""Your Friendly Solution to Managing Browser Cookies

	A convenient tool to store and format browser cookies and use them 
    in 'HTTP' requests (for example, through 'httr2', 'httr' or 'curl').
	"""
	
	cran = "cookiemonster" 

	version("0.0.3", md5="e926f843182d9ad9d80c5d206379ee84")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
