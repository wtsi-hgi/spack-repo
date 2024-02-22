# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodina(RPackage):
	"""Co-Expression Differential Network Analysis

	Categorize links and nodes from multiple networks in 3 categories: Common links (alpha) specific links (gamma), and different links (beta). Also categorizes the links into sub-categories and groups. The package includes a visualization tool for the networks. More information about the methodology can be found at: Gysi et. al., 2018 <arXiv:1802.00828>.
	"""
	
	cran = "CoDiNA" 

	version("1.1.2", md5="d87d74b2d053f4c0f9521284b21daef2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
