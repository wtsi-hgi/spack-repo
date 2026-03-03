# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdendro(RPackage):
	"""Extended Agglomerative Hierarchical Clustering

	A comprehensive collection of linkage methods for agglomerative
  hierarchical clustering on a matrix of proximity data (distances or
  similarities), returning a multifurcated dendrogram or multidendrogram.
  Multidendrograms can group more than two clusters when ties in proximity data
  occur, and therefore they do not depend on the order of the input data.
  Descriptive measures to analyze the resulting dendrogram are additionally
  provided.
	"""
	
	homepage = "https://webs-deim.urv.cat/~sergio.gomez/mdendro.php"
	cran = "mdendro" 

	version("2.2.1", md5="7a010bac5fcb8b9b979be23f17ce843a")

	depends_on("r-rcpp", type=("build", "run"))
