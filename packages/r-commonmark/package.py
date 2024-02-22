# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommonmark(RPackage):
	"""High Performance CommonMark and Github Markdown Rendering in R.

	The CommonMark specification defines a rationalized version of markdown
	syntax. This package uses the 'cmark' reference implementation for
	converting markdown text into various formats including html, latex and
	groff man. In addition it exposes the markdown parse tree in xml format.
	Also includes opt-in support for GFM extensions including tables,
	autolinks, and strikethrough text."""

	cran = "commonmark"

	version("1.9.1", md5="c95e6412ef2937d110128f35fd85be78")

