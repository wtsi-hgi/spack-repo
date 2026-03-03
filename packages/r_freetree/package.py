# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreetree(RPackage):
	"""Tree Method for High Dimensional Longitudinal Data

	This tree-based method deals with high dimensional longitudinal 
	data with correlated features through the use of a piecewise random effect 
	model. FREE tree also exploits the network structure of the features, by 
	first clustering them using Weighted Gene Co-expression Network Analysis 
	('WGCNA'). It then conducts a screening step within each cluster of features 
	and a selecting step among the surviving features, which provides a relatively
	unbiased way to do feature selection. By using dominant principle components 
	as regression variables at each leaf and the original features as splitting 
	variables at splitting nodes, FREE tree delivers easily interpretable results
	while improving computational efficiency.
	"""
	
	cran = "FREEtree" 

	version("0.1.0", md5="541f2e466a84735a6b0b00014fc26a49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmertree", type=("build", "run"))
	depends_on("r-pre", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
