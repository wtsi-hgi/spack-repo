# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBookdown(RPackage):
	"""Authoring Books and Technical Documents with R Markdown.

	Output formats and utilities for authoring books and technical documents
	with R Markdown."""

	cran = "bookdown"

	license("GPL-3.0-only")

	version("0.38", md5="41358aa78abe01e70e121fe317cb7c5f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-knitr@1.38:", type=("build", "run"))
	depends_on("r-rmarkdown@2.14:", type=("build", "run"))
	depends_on("r-jquerylib", type=("build", "run"))
	depends_on("r-xfun@0.39:", type=("build", "run"))
	depends_on("r-tinytex@0.12:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
