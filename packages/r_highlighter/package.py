# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighlighter(RPackage):
	"""Code Syntax Highlighting using the 'Prism.js' Library

	Code Syntax Highlighting made easy for code snippets or complete
    files. Whether you're documenting your data analysis or creating interactive
    'shiny' apps.
	"""
	
	homepage = "https://federiva.github.io/highlighter/"
	cran = "highlighter" 

	version("0.1", md5="0ae3b7ff5b1400b883a63bedfa5ee74e")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
