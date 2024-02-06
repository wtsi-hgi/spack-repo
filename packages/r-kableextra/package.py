# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKableextra(RPackage):
	"""Construct Complex Table with 'kable' and Pipe Syntax.

	Build complex HTML or 'LaTeX' tables using 'kable()' from 'knitr' and the
	piping syntax from 'magrittr'. Function 'kable()' is a light weight table
	generator coming from 'knitr'. This package simplifies the way to
	manipulate the HTML or 'LaTeX' codes generated by 'kable()' and allows
	users to construct complex tables and customize styles using a readable
	syntax."""

	cran = "kableExtra"

	version("1.4.0", md5="94d47966ff22e10e9280f0c39568f7cd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-knitr@1.33:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-xml2@1.1.1:", type=("build", "run"))
	depends_on("r-rmarkdown@1.6:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
