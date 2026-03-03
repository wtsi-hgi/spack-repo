# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymeta(RPackage):
	"""Export Domain Logic from Shiny using Meta-Programming

	Provides tools for capturing logic in a Shiny app and exposing it as code that can be run outside of Shiny (e.g., from an R console). It also provides tools for bundling both the code and results to the end user.
	"""
	
	homepage = "https://rstudio.github.io/shinymeta/"
	cran = "shinymeta" 

	version("0.2.0.3", md5="5452325a791296ba7fb6725d937f9fb0")

	depends_on("r-callr", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-sourcetools", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
