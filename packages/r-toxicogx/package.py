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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ToxicoGx_2.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ToxicoGx/ToxicoGx_2.6.0.tar.gz"]

	version("2.6.0", md5="2be22f48c0e155c94f9af6e6157a0333")

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
