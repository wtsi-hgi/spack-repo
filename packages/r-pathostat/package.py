# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathostat(RPackage):
	"""PathoStat Statistical Microbiome Analysis Package

	The purpose of this package is to perform Statistical Microbiome Analysis on metagenomics results from sequencing data samples. In particular, it supports analyses on the PathoScope generated report files. PathoStat provides various functionalities including Relative Abundance charts, Diversity estimates and plots, tests of Differential Abundance, Time Series visualization, and Core OTU analysis.
	"""
	
	homepage = "https://github.com/mani2012/PathoStat"
	bioc = "PathoStat" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PathoStat_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PathoStat/PathoStat_1.28.0.tar.gz"]

	version("1.28.0", md5="fd391aaf46df86a1608019bd2454d67f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
