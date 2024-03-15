# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkdown(RPackage):
	"""Render Markdown with the C Library 'Sundown'.

	Provides R bindings to the 'Sundown' 'Markdown' rendering library
	(https://github.com/vmg/sundown). 'Markdown' is a plain-text formatting
	syntax that can be converted to 'XHTML' or other formats. See
	https://en.wikipedia.org/wiki/Markdown for more information about
	'Markdown'."""

	cran = "markdown"

	license("MIT")

	version("1.12", md5="cb7221fdb4efa85cdcd15fc871c69889")

	depends_on("r@2.11.1:", type=("build", "run"))
	depends_on("r-commonmark@1.9:", type=("build", "run"))
	depends_on("r-xfun@0.38:", type=("build", "run"))
