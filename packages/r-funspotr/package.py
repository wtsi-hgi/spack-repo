# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunspotr(RPackage):
	"""Spot R Functions & Packages

	Helpers for parsing out the R functions
  and packages used in R scripts and notebooks.
	"""
	
	homepage = "https://brshallo.github.io/funspotr/"
	cran = "funspotr" 

	version("0.0.4", md5="c1f333183070a34de2c344ae8f2b8ceb")

	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-import@1.3:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
