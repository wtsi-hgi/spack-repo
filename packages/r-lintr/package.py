# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLintr(RPackage):
	"""A 'Linter' for R Code

	Checks adherence to a given style, syntax errors and possible
    semantic issues.  Supports on the fly checking of R code edited with
    'RStudio IDE', 'Emacs', 'Vim', 'Sublime Text', 'Atom' and 'Visual
    Studio Code'.
	"""
	
	homepage = "https://github.com/r-lib/lintr"
	cran = "lintr" 

	version("3.1.2", md5="ef1820d613d3ab4d814109ebe21ef897")
	version("3.1.1", md5="8bd97eec8532bedbca25108a9b7b4cea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-backports@1.1.7:", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-cyclocomp", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-xmlparsedata@1.0.5:", type=("build", "run"))
