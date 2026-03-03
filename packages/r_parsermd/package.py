# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParsermd(RPackage):
	"""Formal Parser and Related Tools for R Markdown Documents

	An implementation of a formal grammar and parser for R Markdown documents
    using the Boost Spirit X3 library. It also includes a collection of high level
    functions for working with the resulting abstract syntax tree.
	"""
	
	homepage = "https://rundel.github.io/parsermd/"
	cran = "parsermd" 

	version("0.1.3", md5="0ffd9831307b7567fa12a9c6dfaea5f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cli@2.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
