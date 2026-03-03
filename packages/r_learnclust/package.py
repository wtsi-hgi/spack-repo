# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearnclust(RPackage):
	"""Learning Hierarchical Clustering Algorithms

	Classical hierarchical clustering algorithms, agglomerative and divisive clustering. Algorithms are implemented as a theoretical way, step by step.
  It includes some detailed functions that explain each step. Every function allows options to get different results using different techniques. 
  The package explains non expert users how hierarchical clustering algorithms work.
	"""
	
	cran = "LearnClust" 

	version("1.1", md5="1731b6801d5ea0d00d2235d126e70de8")

	depends_on("r-magick", type=("build", "run"))
