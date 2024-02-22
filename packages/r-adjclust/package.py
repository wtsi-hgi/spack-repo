# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdjclust(RPackage):
	"""Adjacency-Constrained Clustering of a Block-Diagonal Similarity
Matrix

	Implements a constrained version of hierarchical agglomerative 
    clustering, in which each observation is associated to a position, and only 
    adjacent clusters can be merged. Typical application fields in 
    bioinformatics include Genome-Wide Association Studies or Hi-C data 
    analysis, where the similarity between items is a decreasing function of 
    their genomic distance. Taking advantage of this feature, the implemented 
    algorithm is time and memory efficient. This algorithm is described in 
    Ambroise et al (2019) <doi:10.1186/s13015-019-0157-4>.
	"""
	
	homepage = "https://pneuvial.github.io/adjclust/"
	cran = "adjclust" 

	version("0.6.9", md5="877fd57e4800343b303f6057340dd5dc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
