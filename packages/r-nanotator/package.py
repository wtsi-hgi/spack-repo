# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanotator(RPackage):
	"""Next generation structural variant annotation and classification

	Whole genome sequencing (WGS) has successfully been used to identify single-nucleotide variants (SNV), small insertions and deletions (INDELs) and, more recently, small copy number variants (CNVs). However, due to utilization of short reads, it is not well suited for identification of structural variants (SV). Optical mapping (OM) from Bionano Genomics, utilizes long fluorescently labeled megabase size DNA molecules for de novo genome assembly and identification of SVs with a much higher sensitivity than WGS. Nevertheless, currently available SV annotation tools have limited number of functions. NanotatoR is an R package written to provide a set of annotations for SVs identified by OM. It uses Database of Genomic Variants (DGV), Database of Chromosomal Imbalance and Phenotype in Humans Using Ensembl Resources (DECIPHER) as well as a subset (154 samples) of 1000 Genome Project to calculate the population frequencies of the SVs (an optional internal cohort SV frequency calculation is also available). NanotatoR creates a primary gene list (PG) from NCBI databases based on proband’s phenotype specific keywords and compares the list to the set of genes overlapping/near SVs. The output is given in an Excel file format, which is subdivided into multiple sheets based on SV type (e.g., INDELs, Inversions, Translocations). Users then have a choice to filter SVs using the provided annotations for de novo (if parental samples are available) or inherited rare variants.
	"""
	
	homepage = "https://github.com/VilainLab/nanotatoR"
	bioc = "nanotatoR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nanotatoR_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nanotatoR/nanotatoR_1.18.0.tar.gz"]

	version("1.18.0", md5="e808c68591d98effbfdba4dbac07ac91")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-hash@2.2.6:", type=("build", "run"))
	depends_on("r-openxlsx@4.0.17:", type=("build", "run"))
	depends_on("r-rentrez@1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
