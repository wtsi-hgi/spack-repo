# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvest(RPackage):
	"""Easily Harvest (Scrape) Web Pages.

	Wrappers around the 'xml2' and 'httr' packages to make it easy to download,
	then manipulate, HTML and XML."""

	cran = "rvest"

	version("1.0.4", md5="bd391a4e91e6f5867761c99526ffc251")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr@0.5:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-selectr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2@1.3:", type=("build", "run"))
