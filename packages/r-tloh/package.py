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

	version("1.16.0", commit="d1e3d4c93bf3e270049d61404683dc9e6d0e987c")
	version("1.10.0", commit="e14e9c54e0b1aeb401f238c37b1c9bc56ce1bd93")

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
