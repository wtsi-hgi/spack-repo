# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSadeg(RPackage):
	"""Stability Analysis in Differentially Expressed Genes

	We analyzed the nucleotide composition of genes with a special emphasis on stability of DNA sequences. Besides, in a variety of different organisms unequal use of synonymous codons, or codon usage bias, occurs which also show variation among genes in the same genome. Seemingly, codon usage bias is affected by both selective constraints and mutation bias which allows and enables us to examine and detect changes in these two evolutionary forces between genomes or along one genome. Therefore, we determined the codon adaptation index (CAI), effective number of codons (ENC) and codon usage analysis with calculation of the relative synonymous codon usage (RSCU), and subsequently predicted the translation efficiency and accuracy through GC-rich codon usages. Furthermore, we estimated the relative stability of the DNA sequence following calculation of the average free energy (Delta G) and Dimer base-stacking energy level.
	"""
	
	cran = "SADEG" 

	version("1.0.0", md5="73d7245415e2c752a6f06d0f77a08b30")

	depends_on("r@2.10:", type=("build", "run"))
