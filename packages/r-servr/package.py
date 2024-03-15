# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RServr(RPackage):
	"""A Simple HTTP Server to Serve Static Files or Dynamic Documents.

	Start an HTTP server in R to serve static files, or dynamic documents that
	can be converted to HTML files (e.g., R Markdown) under a given
	directory."""

	cran = "servr"

	license("GPL-2.0-or-later")

	version("0.29", md5="76b3ea178083d64a9ed7bb30246e5f4c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mime@0.2:", type=("build", "run"))
	depends_on("r-httpuv@1.5.2:", type=("build", "run"))
	depends_on("r-xfun@0.42:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
