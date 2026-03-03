# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTutorialHelpers(RPackage):
	"""Helper Functions for Creating Tutorials

	Helper functions for creating, editing, and testing tutorials
    created with the 'learnr' package. Provides a simple method for allowing
    students to download their answers to tutorial questions. For examples
    of its use, see the 'r4ds.tutorials' and 'primer.tutorials' packages.
	"""
	
	homepage = "https://ppbds.github.io/tutorial.helpers/"
	cran = "tutorial.helpers" 

	version("0.2.6", md5="e0e9d535103989bed72e554fdaaaa53a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-learnr", type=("build", "run"))
	depends_on("r-parsermd", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
