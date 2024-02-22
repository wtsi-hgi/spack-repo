# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCernaseek(RPackage):
	"""Identification and Analysis of ceRNA Regulation

	Provides several functions to identify and analyse miRNA sponge, including
             popular methods for identifying miRNA sponge interactions, two types 
             of global ceRNA regulation prediction methods and four types of context-specific 
             prediction methods( Li Y et al.(2017) <doi:10.1093/bib/bbx137>), which are based 
             on miRNA-messenger RNA regulation alone, or by integrating heterogeneous data, 
             respectively. In addition, For predictive ceRNA relationship pairs, this package 
             provides several downstream analysis algorithms, including regulatory network 
             analysis and functional annotation analysis, as well as survival prognosis analysis
             based on expression of ceRNA ternary pair. 
	"""
	
	cran = "CeRNASeek" 

	version("2.1.3", md5="9ca8787fb4eba612eac88a074548812a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
