# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyReact(RPackage):
	"""Tools for Using React in Shiny

	
  A toolbox for defining React component wrappers which can be used seamlessly in Shiny apps.
	"""
	
	homepage = "https://appsilon.github.io/shiny.react/"
	cran = "shiny.react" 

	version("0.3.0", md5="96062f94e17bf0107c52c9564e5acd76")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
