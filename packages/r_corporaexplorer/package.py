# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorporaexplorer(RPackage):
	"""A 'Shiny' App for Exploration of Text Collections

	Facilitates dynamic exploration of text collections through an
    intuitive graphical user interface and the power of regular expressions.
    The package contains 1) a helper function to convert a data frame to a
    'corporaexplorerobject', 2) a 'Shiny' app for fast and flexible exploration
    of a 'corporaexplorerobject', and 3) a 'Shiny' app for simple
    retrieval/extraction of documents from a 'corporaexplorerobject' in a
    reading-friendly format. The package also includes demo apps with which
    one can explore Jane Austen's novels and the State of the Union Addresses
    (data from the 'janeaustenr' and 'sotu' packages respectively).
	"""
	
	homepage = "https://kgjerde.github.io/corporaexplorer/"
	cran = "corporaexplorer" 

	version("0.8.6", md5="1d1ab985a4b2450ee3538554eafaf933")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-padr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-re2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
