# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFontawesome(RPackage):
	"""Easily Work with 'Font Awesome' Icons.

	Easily and flexibly insert 'Font Awesome' icons into 'R Markdown' documents
	and 'Shiny' apps. These icons can be inserted into HTML content through
	inline 'SVG' tags or 'i' tags. There is also a utility function for
	exporting 'Font Awesome' icons as 'PNG' images for those situations where
	raster graphics are needed."""

	cran = "fontawesome"

	license("MIT")

	version("0.5.2", md5="d5e7d3d788f1145dd8cb5b74c85045b9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1.1:", type=("build", "run"))
