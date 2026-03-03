# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTomicsvis(RPackage):
	"""Transcriptome Visualization Process Scheme

	Transcriptome visualization from sample trait statistics to gene expression analysis. Six categories include "Samples Statistics", "Traits Analysis", "Differential Expression Analysis", "Advanced Analysis", "GO and KEGG Enrichment", "Tables Operations", with complete sample data.
	"""
	
	homepage = "https://benben-miao.github.io/TOmicsVis/"
	cran = "TOmicsVis" 

	version("2.0.0", md5="4073d31fdb51b1018c6e659c6565b379")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-e1071@1.7.0:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-venn", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-enhancedvolcano", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggpolypath", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-mfuzz", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
