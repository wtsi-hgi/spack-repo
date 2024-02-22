# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardelino(RPackage):
	"""Clone Identification from Single Cell Data

	Methods to infer clonal tree configuration for a population of cells using single-cell RNA-seq data (scRNA-seq), and possibly other data modalities. Methods are also provided to assign cells to inferred clones and explore differences in gene expression between clones. These methods can flexibly integrate information from imperfect clonal trees inferred based on bulk exome-seq data, and sparse variant alleles expressed in scRNA-seq data. A flexible beta-binomial error model that accounts for stochastic dropout events as well as systematic allelic imbalance is used.
	"""
	
	homepage = "https://github.com/single-cell-genetics/cardelino"
	bioc = "cardelino" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cardelino_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cardelino/cardelino_1.4.0.tar.gz"]

	version("1.4.0", md5="363c06547419f29e1cdfe473651e1861")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
