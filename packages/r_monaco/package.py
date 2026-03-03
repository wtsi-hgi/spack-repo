# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonaco(RPackage):
	"""The 'Monaco' Editor as a HTML Widget

	A HTML widget rendering the 'Monaco' editor. The 'Monaco' editor is the code editor which powers 'VS Code'. It is particularly well developed for 'JavaScript'. In addition to the built-in features of the 'Monaco' editor, the widget allows to prettify multiple languages, to view the 'HTML' rendering of 'Markdown' code, and to view and resize 'SVG' images.
	"""
	
	homepage = "https://github.com/stla/monaco"
	cran = "monaco" 

	version("0.2.2", md5="3b677c2bd936fae476c2472f46ec3fa6")

	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
