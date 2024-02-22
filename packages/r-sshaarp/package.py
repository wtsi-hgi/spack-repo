# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSshaarp(RPackage):
	"""Searching Shared HLA Amino Acid Residue Prevalence

	Processes amino acid alignments produced by the 'IPD-IMGT/HLA (Immuno Polymorphism-ImMunoGeneTics/Human Leukocyte Antigen) Database' to identify user-defined amino acid residue motifs shared across HLA alleles, and calculates the frequencies of those motifs based on HLA allele frequency data. 'SSHAARP' (Searching Shared HLA Amino Acid Residue Prevalence) uses 'Generic Mapping Tools (GMT)' software and the 'GMT' R package to generate global frequency heat maps that illustrate the distribution of each user-defined map around the globe. 'SSHAARP' analyzes the allele frequency data described by Solberg et al. (2008) <doi:10.1016/j.humimm.2008.05.001>, a global set of 497 population samples from 185 published datasets, representing 66,800 individuals total.
	"""
	
	cran = "SSHAARP" 

	version("1.1.0", md5="0220479a09fb8723189611d7f2a09db0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-bigdawg", type=("build", "run"))
	depends_on("r-gmt", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-filesstrings", type=("build", "run"))
	depends_on("gmt@5:", type=("build", "link", "run"))
	depends_on("ghostscript@9.6:", type=("build", "link", "run"))
