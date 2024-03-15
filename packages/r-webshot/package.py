# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebshot(RPackage):
	"""Take Screenshots of Web Pages.

	Takes screenshots of web pages, including Shiny applications and R Markdown
	documents."""

	cran = "webshot"

	license("GPL-2.0-only")

	version("0.5.5", md5="72d833c018161458889af9d9aae8f399")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))

	# need a phantomjs package to make this actually work.
