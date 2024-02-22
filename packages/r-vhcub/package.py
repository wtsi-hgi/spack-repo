# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVhcub(RPackage):
	"""Virus-Host Codon Usage Co-Adaptation Analysis

	Analyze the co-adaptation of codon usage between a virus and its host, calculate various codon usage bias measurements as: effective number of codons (ENc) Novembre (2002) <doi:10.1093/oxfordjournals.molbev.a004201>, codon adaptation index (CAI) Sharp  and  Li (1987) <doi:10.1093/nar/15.3.1281>, relative  codon deoptimization index (RCDI) Puigbò et al (2010) <doi:10.1186/1756-0500-3-87>, similarity index (SiD) Zhou et al (2013) <doi:10.1371/journal.pone.0077239>,  synonymous codon usage orderliness (SCUO) Wan et al (2004) <doi:10.1186/1471-2148-4-19> and, relative synonymous    codon usage (RSCU) Sharp et al (1986) <doi:10.1093/nar/14.13.5125>. Also, it provides a statistical dinucleotide over- and underrepresentation with three different models. Implement several methods for visualization of codon usage as ENc.GC3plot() and PR2.plot().
	"""
	
	cran = "vhcub" 

	version("1.0.0", md5="52fbb03f7cb28b6701eff95622eee124")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-cordon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
