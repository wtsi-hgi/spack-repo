# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsconnect(RPackage):
	"""Deployment Interface for R Markdown Documents and Shiny Applications.

	Programmatic deployment interface for 'RPubs', 'shinyapps.io', and 'RStudio
	Connect'. Supported content types include R Markdown documents, Shiny
	applications, Plumber APIs, plots, and static web content."""

	cran = "rsconnect"

	version("1.2.1", md5="ebf2f8654e76fde69636715277afd745")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-openssl@2:", type=("build", "run"))
	depends_on("r-packrat@0.6:", type=("build", "run"))
	depends_on("r-renv@1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
	depends_on("r-yaml@2.1.5:", type=("build", "run"))
