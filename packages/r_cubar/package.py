# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubar(RPackage):
	"""Codon Usage Bias Analysis

	A suite of functions for rapid and flexible analysis of codon 
    usage bias. It provides in-depth analysis at the codon level, including 
    relative synonymous codon usage (RSCU), tRNA weight calculations, machine 
    learning predictions for optimal or preferred codons, and visualization of 
    codon-anticodon pairing. Additionally, it can calculate various gene-
    specific codon indices such as codon adaptation index (CAI), effective 
    number of codons (ENC), fraction of optimal codons (Fop), tRNA adaptation 
    index (tAI), mean codon stabilization coefficients (CSCg), and GC contents 
    (GC/GC3s/GC4d). It also supports both standard and non-standard genetic 
    code tables found in NCBI, as well as custom genetic code tables.
	"""
	
	homepage = "https://github.com/mt1022/cubar"
	cran = "cubar" 

	version("0.5.0", md5="23b526d6dd9cc16cca52580e4eed255e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biostrings@2.60:", type=("build", "run"))
	depends_on("r-iranges@2.34:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
