# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierbipartite(RPackage):
	"""Bipartite Graph-Based Hierarchical Clustering

	
    Bipartite graph-based hierarchical clustering, developed for pharmacogenomic 
    datasets and datasets sharing the same data structure. The goal is to 
    construct a hierarchical clustering of groups of samples based on 
    association patterns between two sets of variables. In the context of
    pharmacogenomic datasets, the samples are cell lines, and the two sets of 
    variables are typically expression levels and drug sensitivity values. 
    For this method, sparse canonical correlation analysis from 
    Lee, W., Lee, D., Lee, Y. and Pawitan, Y. (2011) <doi:10.2202/1544-6115.1638> 
    is first applied to extract association patterns for each group of samples. 
    Then, a nuclear norm-based dissimilarity measure is used to construct a 
    dissimilarity matrix between groups based on the extracted associations. 
    Finally, hierarchical clustering is applied.
	"""
	
	cran = "hierBipartite" 

	version("0.0.2", md5="cd31c853f3611d74f4c53dbd5f47bce3")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
