# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToxicogx(RPackage):
	"""Analysis of Large-Scale Toxico-Genomic Data

	Contains a set of functions to perform large-scale analysis of toxicogenomic data, providing a standardized data structure to hold information relevant to annotation, visualization and statistical analysis of toxicogenomic data.
	"""
	
	bioc = "ToxicoGx"

	version("2.12.0", commit="0f379b8abe2938e983638e1c9f131ffcb6e5ca29")
	version("2.6.0", commit="b6bd52096eb2f6b09fefa052d3972e75e8bf8e83")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-coregx", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
