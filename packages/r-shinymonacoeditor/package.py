# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymonacoeditor(RPackage):
	"""The 'Monaco' Editor in 'Shiny'

	A 'Shiny' app including the 'Monaco' editor. The 'Monaco' editor is the code editor which powers 'VS Code'. It is particularly well developed for 'JavaScript'. In addition to the 'Monaco' editor features, the app provides prettifiers and minifiers for multiple languages, 'SCSS' and 'TypeScript' compilers, code checking for 'C' and 'C++' (requires 'cppcheck').
	"""
	
	homepage = "https://github.com/stla/shinyMonacoEditor"
	cran = "shinyMonacoEditor" 

	version("1.1.0", md5="261e55576ea8121ad1f36dcc6a9360ac")

	depends_on("r-shiny", type=("build", "run"))
