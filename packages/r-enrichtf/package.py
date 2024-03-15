# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnrichtf(RPackage):
	"""Transcription Factors Enrichment Analysis

	As transcription factors (TFs) play a crucial role in regulating the transcription process through binding on the genome alone or in a combinatorial manner, TF enrichment analysis is an efficient and important procedure to locate the candidate functional TFs from a set of experimentally defined regulatory regions. While it is commonly accepted that structurally related TFs may have similar binding preference to sequences (i.e. motifs) and one TF may have multiple motifs, TF enrichment analysis is much more challenging than motif enrichment analysis. Here we present a R package for TF enrichment analysis which combine motif enrichment with the PECA model.
	"""
	
	homepage = "https://github.com/wzthu/enrichTF"
	bioc = "enrichTF" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/enrichTF_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/enrichTF/enrichTF_1.18.0.tar.gz"]

	version("1.18.0", md5="a88296c9418e41a8e66fccc276925471")

	depends_on("r-pipeframe", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-jaspar2018", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-heatmap3", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
