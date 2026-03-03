# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProgenyclust(RPackage):
	"""Finding the Optimal Cluster Number Using Progeny Clustering

	Implementing the Progeny Clustering algorithm, the 'progenyClust' package assesses the clustering stability and identifies the optimal clustering number for a given data matrix. It uses k-means clustering as a default, provides a tailored hierarchical clustering function, and can be customized to work with other clustering algorithms and different parameter settings. The package includes a main function progenyClust(), plot and summary methods for 'progenyClust' object, a function hclust.progenyClust() for hierarchical clustering, and two example datasets (test and cell) for testing. 
	"""
	
	cran = "progenyClust" 

	version("1.2", md5="621eff5788c45d375b668c1357bdfd54")

	depends_on("r-hmisc", type=("build", "run"))
