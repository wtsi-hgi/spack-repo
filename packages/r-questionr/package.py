# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuestionr(RPackage):
	"""Functions to Make Surveys Processing Easier.

	Set of functions to make the processing and analysis of surveys easier:
	interactive shiny apps and addins for data recoding, contingency tables,
	dataset metadata handling, and several convenience functions."""

	cran = "questionr"

	license("GPL-2.0-or-later")

	version("0.7.8", md5="d9c03e4ed2f6345d7ee174c6348a872d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.0.5:", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-highr", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-labelled@2.6:", type=("build", "run"))
	depends_on("xclip", type=("build", "link", "run"))
