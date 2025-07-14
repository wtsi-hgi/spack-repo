# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGranie(RPackage):
	"""GRaNIE: Reconstruction cell type specific gene regulatory networks including enhancers using chromatin accessibility and RNA-seq data

	Genetic variants associated with diseases often affect non-coding regions, thus likely having a regulatory role. To understand the effects of genetic variants in these regulatory regions, identifying genes that are modulated by specific regulatory elements (REs) is crucial. The effect of gene regulatory elements, such as enhancers, is often cell-type specific, likely because the combinations of transcription factors (TFs) that are regulating a given enhancer have celltype specific activity. This TF activity can be quantified with existing tools such as diffTF and captures differences in binding of a TF in open chromatin regions. Collectively, this forms a gene regulatory network (GRN) with cell-type and data-specific TF-RE and RE-gene links. Here, we reconstruct such a GRN using bulk RNAseq and open chromatin (e.g., using ATACseq or ChIPseq for open chromatin marks) and optionally TF activity data. Our network contains different types of links, connecting TFs to regulatory elements, the latter of which is connected to genes in the vicinity or within the same chromatin domain (TAD). We use a statistical framework to assign empirical FDRs and weights to all links using a permutation-based approach.
	"""
	
	homepage = "https://grp-zaugg.embl-community.io/GRaNIE"
	bioc = "GRaNIE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GRaNIE_1.6.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GRaNIE/GRaNIE_1.6.1.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.1", sha256="681f6cd397a1861871fedcbc84b69e5cfe86db7bb5493bd69d9eb1e2b43d37ed")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb@1.34.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
