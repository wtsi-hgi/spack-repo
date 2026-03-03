# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnectwidgets(RPackage):
	"""Organize and Curate Your Content Within 'Posit Connect'

	A collection of helper functions and 'htmlwidgets' to help publishers
    curate content collections on 'Posit Connect'. The components,
    Card, Grid, Table, Search, and Filter can be used to produce a
    showcase page or gallery contained within a static or interactive
    R Markdown page.
	"""
	
	homepage = "https://rstudio.github.io/connectwidgets/"
	cran = "connectwidgets" 

	version("0.2.1", md5="66d49a0ebe3729c74683a1fc2c0e1f66")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
