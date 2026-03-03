# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalclusteringtree(RPackage):
	"""Clustering Analysis Using Survival Tree and Forest Algorithms

	An outcome-guided algorithm is developed to identify clusters of samples with similar characteristics and survival rate. The algorithm first builds a random forest and then defines distances between samples based on the fitted random forest. Given the distances, we can apply hierarchical clustering algorithms to define clusters. Details about this method is described in <https://github.com/luyouepiusf/SurvivalClusteringTree>.
	"""
	
	cran = "SurvivalClusteringTree" 

	version("1.0", md5="5273aacdc0a253ae38790cdb35c33b96")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridtext", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
