# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGemmaR(RPackage):
	"""A wrapper for Gemma's Restful API to access curated gene expression data and differential expression analyses

	Low- and high-level wrappers for Gemma's RESTful API. They enable access to curated expression and differential expression data from over 10,000 published studies. Gemma is a web site, database and a set of tools for the meta-analysis, re-use and sharing of genomics data, currently primarily targeted at the analysis of gene expression profiles.
	"""
	
	homepage = "https://pavlidislab.github.io/gemma.R/"
	bioc = "gemma.R" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gemma.R_2.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gemma.R/gemma.R_2.0.0.tar.gz"]

	version("2.0.0", sha256="0524f520b5b6f63438b35157be3eb35b981d4c431e54081070d3cdfd57d095cd")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
