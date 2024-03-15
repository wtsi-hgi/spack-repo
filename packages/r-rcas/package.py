# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcas(RPackage):
	"""RNA Centric Annotation System

	RCAS is an R/Bioconductor package designed as a generic reporting tool for the functional analysis of transcriptome-wide regions of interest detected by high-throughput experiments. Such transcriptomic regions could be, for instance, signal peaks detected by CLIP-Seq analysis for protein-RNA interaction sites, RNA modification sites (alias the epitranscriptome), CAGE-tag locations, or any other collection of query regions at the level of the transcriptome. RCAS produces in-depth annotation summaries and coverage profiles based on the distribution of the query regions with respect to transcript features (exons, introns, 5'/3' UTR regions, exon-intron boundaries, promoter regions). Moreover, RCAS can carry out functional enrichment analyses and discriminative motif discovery.
	"""
	
	bioc = "RCAS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RCAS_1.28.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RCAS/RCAS_1.28.3.tar.gz"]

	version("1.28.3", md5="ed2c97bacd70c083df386e7df14d0c11")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotly@4.5.2:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-genomeinfodb@1.12:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rmarkdown@0.9.5:", type=("build", "run"))
	depends_on("r-genomation@1.5.5:", type=("build", "run"))
	depends_on("r-knitr@1.12.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
	depends_on("r-ggseqlogo", type=("build", "link", "run"))
