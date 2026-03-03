# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlow(RPackage):
	"""View and Browse Code Using Flow Diagrams

	Visualize as flow diagrams the logic of functions, expressions or 
  scripts in a static way or when running a call, visualize the dependencies between
  functions or between modules in a shiny app, and more.
	"""
	
	homepage = "https://github.com/moodymudskipper/flow"
	cran = "flow" 

	version("0.2.0", md5="ddf306474b8eca349d2bbb5d63f1877c")

	depends_on("r-nomnoml", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
