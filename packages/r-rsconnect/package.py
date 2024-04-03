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
	version("0.8.29", sha256="852899d2aaf90bcedf4d191a9e00c770e8ee4233235169fc97e6aa636de01c43")
	version("0.8.28", sha256="25b9a947772ada9593da5c48297b7a7dd0e11aa73fbb9a282631c75ec49616e0")
	version("0.8.27", sha256="0a44d5605fc7cd6855ea0235d662e4a323a24a2c214cc4f1696afbca3a8f169c")
	version("0.8.26", sha256="faafabbed803743799b345051f221aef2b4497b421fc98092ca41c05ef6b5fed")
	version("0.8.25", sha256="3c055277f745f2ca37a73e2f425249307cea4dc95ecc59fbe05ee8b6cf26d9cf")
	version("0.8.17", sha256="64767a4d626395b7871375956a9f0455c3d64ff6e779633b0e554921d85da231")
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
