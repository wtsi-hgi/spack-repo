# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSketch(RPackage):
	"""Interactive Sketches

	Creates static / animated / interactive visualisations embeddable
    in R Markdown documents. It implements an R-to-JavaScript transpiler and
    enables users to write JavaScript applications using the syntax of R.
	"""
	
	cran = "sketch" 

	version("1.1.20.3", md5="fd09db4c81a03b7240c84e78db46d8cf")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
