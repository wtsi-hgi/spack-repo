# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqgene(RPackage):
	"""RNA-seq workflow: gene-level exploratory analysis and differential expression

	Here we walk through an end-to-end gene-level RNA-seq differential expression workflow using Bioconductor packages. We will start from the FASTQ files, show how these were aligned to the reference genome, and prepare a count matrix which tallies the number of RNA-seq reads/fragments within each gene for each sample.  We will perform exploratory data analysis (EDA) for quality assessment and to explore the relationship between samples, perform differential gene expression analysis, and visually explore the results.
	"""
	
	homepage = "https://github.com/thelovelove/rnaseqGene/"
	bioc = "rnaseqGene"

	version("1.32.0", commit="f09044c2f535e228b3ddd88a06385f92e3bf5f07")
	version("1.26.0", commit="eb0ccb5c755d0d06f5fffa7c6d70ff39a16ef348")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-airway@1.5.3:", type=("build", "run"))
	depends_on("r-tximeta", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-apeglm", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-poiclaclu", type=("build", "run"))
	depends_on("r-glmpca", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-reportingtools", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-ruvseq", type=("build", "run"))
	depends_on("r-fission", type=("build", "run"))

