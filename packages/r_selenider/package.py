# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelenider(RPackage):
	"""Concise, Lazy and Reliable Wrapper for 'chromote' and 'selenium'

	A user-friendly wrapper for web automation, using either 'chromote'
    or 'selenium'. Provides a simple and consistent API to make web scraping
    and testing scripts easy to write and understand. Elements are lazy, and
    automatically wait for the website to be valid, resulting in reliable and
    reproducible code, with no visible impact on the experience of the
    programmer.
	"""
	
	homepage = "https://github.com/ashbythorpe/selenider"
	cran = "selenider" 

	version("0.3.0", md5="7fd701019aabad6e94dc7447c15a1332")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
