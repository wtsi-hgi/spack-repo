# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdos(RPackage):
	"""Integrated Discovery of Oncogenic Signatures

	A method to integrate molecular profiles of cancer patients (gene copy number and mRNA abundance) to 
	identify candidate gain of function alterations. These candidate alterations can be subsequently further tested  
	to discover cancer driver alterations. Briefly, this method tests of genomic correlates of mRNA dysregulation and prioritise 
	those where DNA gains/amplifications are associated with elevated mRNA expression of the same gene. For details see,
	Haider S et al. (2016) "Genomic alterations underlie a pan-cancer metabolic shift associated with tumour hypoxia", Genome Biology, <https://pubmed.ncbi.nlm.nih.gov/27358048/>.
	"""
	
	cran = "iDOS" 

	version("1.0.1", md5="e6f6b6a51d6e592aa75eb6703da1562f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-venndiagram@1.6.5:", type=("build", "run"))
