# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgvis(RPackage):
	"""Interactive Grammar of Graphics.

	An implementation of an interactive grammar of graphics, taking the best
	parts of 'ggplot2', combining them with the reactive framework from 'shiny'
	and web graphics from 'vega'."""

	cran = "ggvis"

	license("GPL-2.0-only OR custom")

	version("0.4.9", md5="cd8e7cebdac79ce1925e39f4072900cb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-htmltools@0.2.4:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.11:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny@0.11.1:", type=("build", "run"))
