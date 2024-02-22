# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoharp(RPackage):
	"""Semi-Automatic Grading of R and Rmd Scripts

	A customisable set of tools for assessing and grading 
    R or R-markdown scripts from students. It allows for checking correctness 
    of code output, runtime statistics and static code analysis. The latter 
    feature is made possible by representing R expressions using a tree
    structure.
	"""
	
	homepage = "https://singator.github.io/autoharp-docs/"
	cran = "autoharp" 

	version("0.0.10", md5="1c80791fbf449503c8a44bd0e5012bf9")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-lintr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
