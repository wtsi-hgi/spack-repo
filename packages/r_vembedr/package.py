# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVembedr(RPackage):
	"""Embed Video in HTML

	A set of functions for generating HTML to
    embed hosted video in your R Markdown documents or Shiny applications.
	"""
	
	homepage = "https://github.com/ijlyttle/vembedr"
	cran = "vembedr" 

	version("0.1.5", md5="462e9fa8872be90ef44f2e42e933a9b5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
