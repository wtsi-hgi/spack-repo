# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAceeditor(RPackage):
	"""The 'Ace' Editor as a HTML Widget

	Wraps the 'Ace' editor in a HTML widget. The 'Ace' editor has support for many languages. It can be opened in the viewer pane of 'RStudio', and this provides a second source editor.
	"""
	
	homepage = "https://github.com/stla/aceEditor"
	cran = "aceEditor" 

	version("1.0.1", md5="2470634265562e4c6caa37a383d36822")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
