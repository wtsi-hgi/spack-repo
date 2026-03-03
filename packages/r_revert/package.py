# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevert(RPackage):
	"""Reversion Mutation Identifier for Sequencing Data

	A tool for detecting reversions for a given pathogenic mutation from 
	next-generation DNA sequencing data. It analyses reads aligned to the locus of the 
	pathogenic mutation and reports reversion events where secondary mutations have 
	restored or undone the deleterious effect of the original pathogenic mutation, e.g., 
	secondary indels complement to a frameshift pathogenic mutation converting the 
	orignal frameshift mutation into inframe mutaions, deletions or SNVs that replaced 
	the original pathogenic mutation restoring the open reading frame, SNVs changing the 
	stop codon caused by the original nonsense SNV into an amino acid, etc.
	"""
	
	cran = "revert" 

	version("0.0.1", md5="654da932a1702fcd3d1e71962c36f4e3")

	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))
	depends_on("r@4.1.0:", type=("build", "link", "run"))
	depends_on("samtools@1.11:", type=("build", "link", "run"))
