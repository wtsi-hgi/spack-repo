# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTloh(RPackage):
	"""Assessment of evidence for LOH in spatial transcriptomics pre-processed data using Bayes factor calculations

	tLOH, or transcriptomicsLOH, assesses evidence for loss of heterozygosity (LOH) in pre-processed spatial transcriptomics data. This tool requires spatial transcriptomics cluster and allele count information at likely heterozygous single-nucleotide polymorphism (SNP) positions in VCF format. Bayes factors are calculated at each SNP to determine likelihood of potential loss of heterozygosity event. Two plotting functions are included to visualize allele fraction and aggregated Bayes factor per chromosome. Data generated with the 10X Genomics Visium Spatial Gene Expression platform must be pre-processed to obtain an individual sample VCF with columns for each cluster. Required fields are allele depth (AD) with counts for reference/alternative alleles and read depth (DP).
	"""
	
	homepage = "https://github.com/USCDTG/tLOH"
	bioc = "tLOH" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/tLOH_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/tLOH/tLOH_1.10.0.tar.gz"]

	version("1.10.0", md5="1693fc28c2855f1af11159ec1051e2df")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-bestnormalize", type=("build", "run"))
	depends_on("r-depmixs4", type=("build", "run"))
	depends_on("r-naniar", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
