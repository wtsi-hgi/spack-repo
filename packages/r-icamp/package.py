# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcamp(RPackage):
	"""Infer Community Assembly Mechanisms by Phylogenetic-Bin-Based
Null Model Analysis

	To implement a general framework to quantitatively infer Community Assembly Mechanisms by Phylogenetic-bin-based null model analysis, abbreviated as 'iCAMP' (Ning et al 2020) <doi:10.1038/s41467-020-18560-z>. It can quantitatively assess the relative importance of different community assembly processes, such as selection, dispersal, and drift, for both communities and each phylogenetic group ('bin'). Each bin usually consists of different taxa from a family or an order. The package also provides functions to implement some other published methods, including neutral taxa percentage (Burns et al 2016) <doi:10.1038/ismej.2015.142> based on neutral theory model and quantifying assembly processes based on entire-community null models ('QPEN', Stegen et al 2013) <doi:10.1038/ismej.2013.93>. It also includes some handy functions, particularly for big datasets, such as phylogenetic and taxonomic null model analysis at both community and bin levels, between-taxa niche difference and phylogenetic distance calculation, phylogenetic signal test within phylogenetic groups, midpoint root of big trees, etc. Version 1.3.x mainly improved the function for 'QPEN' and added function 'icamp.cate()' to summarize 'iCAMP' results for different categories of taxa (e.g. core versus rare taxa).
	"""
	
	homepage = "https://github.com/DaliangNing/iCAMP1"
	cran = "iCAMP" 

	version("1.5.12", md5="daad4a7f7a4b39244bdfb9076792dcba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-dirichletreg", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
