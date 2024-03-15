# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettifyaddins(RPackage):
	"""'RStudio' Addins to Prettify 'JavaScript', 'C++', 'Python', and
More

	Provides 'RStudio' addins to prettify 'HTML', 'CSS', 'SCSS',
    'JavaScript', 'JSX', 'Markdown', 'C(++)', 'LaTeX', 'Python', 'Julia',
    'XML', 'Java', 'JSON', 'Ruby', and to reindent 'C(++)', 'Fortran',
    'Java', 'Julia', 'Python', 'SAS', 'Scala', 'Shell', 'SQL' and
    "TypeScript". Two kinds of addins are provided: 'Prettify' and
    'Indent'. The 'Indent' addins only reindent the code, while the
    'Prettify' addins also modify the code, e.g. trailing semi-colons are
    added to 'JavaScript' code when they are missing.
	"""
	
	homepage = "https://github.com/stla/prettifyAddins"
	cran = "prettifyAddins" 

	version("2.6.1", md5="0048bb530862d489c4689884f2e59538")

	depends_on("r-chromote", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-webdriver", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xrjulia", type=("build", "run"))
