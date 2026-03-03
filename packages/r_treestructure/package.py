# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreestructure(RPackage):
	"""Detect Population Structure Within Phylogenetic Trees

	Algorithms for detecting population structure from the history of coalescent events recorded in phylogenetic trees. This method classifies each tip and internal node of a tree into disjoint sets characterized by similar coalescent patterns. The methods are described in Volz, E., Wiuf, C., Grad, Y., Frost, S., Dennis, A., & Didelot, X. (2020) <doi:10.1093/sysbio/syaa009>.
	"""
	
	cran = "treestructure" 

	version("0.1.0", md5="eb77dec05f3a63c14c7bc917ab0e3388")

	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
