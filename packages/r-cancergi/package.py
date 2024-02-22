# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancergi(RPackage):
	"""Analyses of Cancer Gene Interaction

	Functions to perform the following analyses: i) inferring epistasis from RNAi double knockdown data; ii) identifying gene pairs of multiple mutation patterns; iii) assessing association between gene pairs and survival; and iv) calculating the smallworldness of a graph (e.g., a gene interaction network).  Data and analyses are described in Wang, X., Fu, A. Q., McNerney, M. and White, K. P. (2014). Widespread genetic epistasis among breast cancer genes. Nature Communications. 5 4828. <doi:10.1038/ncomms5828>.
	"""
	
	cran = "cancerGI" 

	version("1.0.1", md5="1174b7c39ed03874f4e528e86e9908b9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
