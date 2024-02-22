# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMia(RPackage):
	"""Microbiome analysis

	mia implements tools for microbiome analysis based on the SummarizedExperiment, SingleCellExperiment and TreeSummarizedExperiment infrastructure. Data wrangling and analysis in the context of taxonomic data is the main scope. Additional functions for common task are implemented such as community indices calculation and summarization.
	"""
	
	homepage = "https://github.com/microbiome/mia"
	bioc = "mia" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mia_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mia/mia_1.10.0.tar.gz"]

	version("1.10.0", md5="73446335fd354444f38c4e8cf793d520")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-treesummarizedexperiment@1.99.3:", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-decontam", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-decipher", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-dirichletmultinomial", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bluster", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
