# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataValidator(RPackage):
	"""Automatic Data Validation and Reporting

	Validate dataset by columns and rows using convenient predicates inspired by 'assertr' package.
             Generate good looking HTML report or print console output to display in logs of your data processing pipeline.
	"""
	
	homepage = "https://appsilon.github.io/data.validator/"
	cran = "data.validator" 

	version("0.2.1", md5="d47878e30f464f1d29b13b8990fff5da")

	depends_on("r-assertr@2.8:", type=("build", "run"))
	depends_on("r-shiny-semantic@0.3.3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
