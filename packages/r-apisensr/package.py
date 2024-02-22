# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApisensr(RPackage):
	"""Interface to 'episensr' for Sensitivity Analysis of
Epidemiological Results

	API for using 'episensr', Basic sensitivity analysis of the observed relative risks adjusting for unmeasured confounding and misclassification of the exposure/outcome, or both. See <https://cran.r-project.org/package=episensr>.
	"""
	
	homepage = "https://github.com/dhaine/apisensr"
	cran = "apisensr" 

	version("1.0.0", md5="7dc74acd46a1ac1b4db87c4a14d01cf4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-episensr@1.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinymaterial", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
