# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReportfactory(RPackage):
	"""Lightweight Infrastructure for Handling Multiple R Markdown
Documents

	Provides an infrastructure for handling multiple R Markdown
  reports, including automated curation and time-stamping of outputs,
  parameterisation and provision of helper functions to manage dependencies.
	"""
	
	homepage = "https://github.com/reconverse/reportfactory"
	cran = "reportfactory" 

	version("0.4.0", md5="94bacc7b3dfdd42249bf907855677768")

	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
