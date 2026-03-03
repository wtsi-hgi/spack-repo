# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobotstxt(RPackage):
	"""A 'robots.txt' Parser and 'Webbot'/'Spider'/'Crawler'
Permissions Checker

	Provides functions to download and parse 'robots.txt' files.
        Ultimately the package makes it easy to check if bots
        (spiders, crawler, scrapers, ...) are allowed to access specific
        resources on a domain.
	"""
	
	homepage = "https://docs.ropensci.org/robotstxt/"
	cran = "robotstxt" 

	version("0.7.13", md5="92378e6fc64e005cdac4f35599792f07")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-spiderbar@0.2:", type=("build", "run"))
	depends_on("r-future@1.6.2:", type=("build", "run"))
	depends_on("r-future-apply@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
