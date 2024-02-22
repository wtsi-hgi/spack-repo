# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugsim2dr(RPackage):
	"""Predict Drug Functional Similarity to Drug Repurposing

	A systematic biology tool was developed to repurpose drugs via a drug-drug functional similarity network. 'DrugSim2DR' first predict drug-drug functional similarity  in the context of specific disease, and then using the similarity constructed a weighted drug similarity network. Finally, it used a network propagation algorithm on the network to identify drugs with significant target abnormalities as candidate drugs.
	"""
	
	cran = "DrugSim2DR" 

	version("0.1.1", md5="c02eaf39663041e09a38b37729d29b4d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
