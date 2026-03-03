# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegreport(RPackage):
	"""Report of DEG analysis

	Creation of a HTML report of differential expression analyses of count data. It integrates some of the code mentioned in DESeq2 and edgeR vignettes, and report a ranked list of genes according to the fold changes mean and variability for each selected gene.
	"""
	
	homepage = "http://lpantano.github.io/DEGreport/"
	bioc = "DEGreport" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DEGreport_1.38.5.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DEGreport/DEGreport_1.38.5.tar.gz"]

	version("1.38.5", md5="c244b736c180d78d142dd00938f7d40f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-logging", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
