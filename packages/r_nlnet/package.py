# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlnet(RPackage):
	"""Nonlinear Network, Clustering, and Variable Selection Based on
DCOL

	It includes four methods: DCOL-based K-profiles clustering, non-linear network reconstruction, non-linear hierarchical clustering, and variable selection for generalized additive model. References:  Tianwei Yu (2018)<DOI: 10.1002/sam.11381>; Haodong Liu and others (2016)<DOI: 10.1371/journal.pone.0158247>; Kai Wang and others (2015)<DOI: 10.1155/2015/918954>; Tianwei Yu and others (2010)<DOI: 10.1109/TCBB.2010.73>.
	"""
	
	cran = "nlnet" 

	version("1.4", md5="1234e1b474252bcf756adf5c01160713")

	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
