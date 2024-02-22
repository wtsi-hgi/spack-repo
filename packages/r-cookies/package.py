# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCookies(RPackage):
	"""Use Browser Cookies with 'shiny'

	Browser cookies are name-value pairs that are saved in a
    user's browser by a website. Cookies allow websites to persist
    information about the user and their use of the website. Here we
    provide tools for working with cookies in 'shiny' apps, in part by
    wrapping the 'js-cookie' JavaScript library
    <https://github.com/js-cookie/js-cookie>.
	"""
	
	homepage = "https://github.com/r4ds/cookies"
	cran = "cookies" 

	version("0.2.3", md5="ce331ad5a66add822456c69ffaf8fb4f")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clock", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
