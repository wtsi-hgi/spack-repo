# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValerie(RPackage):
	"""Visualising Splicing at Single-Cell Resolution

	Alternative splicing produces a variety of different protein products from a given gene. 'VALERIE' enables visualisation of alternative splicing events from high-throughput single-cell RNA-sequencing experiments. 'VALERIE' computes percent spliced-in (PSI) values for user-specified genomic coordinates corresponding to alternative splicing events. PSI is the proportion of sequencing reads supporting the included exon/intron as defined by Shiozawa (2018) <doi:10.1038/s41467-018-06063-x>. PSI are inferred from sequencing reads data based on specialised infrastructures for representing and computing annotated genomic ranges by Lawrence (2013) <doi:10.1371/journal.pcbi.1003118>. Computed PSI for each single cell are subsequently presented in the form of a heatmap implemented using the 'pheatmap' package by Kolde (2010) <https://CRAN.R-project.org/package=pheatmap>. Board overview of the mean PSI difference and associated p-values across different user-defined groups of single cells are presented in the form of a line graph using the 'ggplot2' package by Wickham (2007) <https://CRAN.R-project.org/package=ggplot2>.
	"""
	
	cran = "VALERIE" 

	version("1.1.0", md5="c13838447024ea90ff08eb5210a76c8f")

	depends_on("r-genomicalignments@1.16:", type=("build", "run"))
	depends_on("r-genomicranges@1.32:", type=("build", "run"))
	depends_on("r-iranges@2.14:", type=("build", "run"))
	depends_on("r-rsamtools@1.34:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-pheatmap@1.0.10:", type=("build", "run"))
	depends_on("r-ggplotify@0.0.3:", type=("build", "run"))
	depends_on("r-ggpubr@0.2.4:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
