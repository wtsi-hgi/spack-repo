# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrsim(RPackage):
	"""Brainerd-Robinson Similarity Coefficient Matrix

	Provides the facility to calculate the Brainerd-Robinson similarity coefficient for the rows of an input table, and to calculate the significance of each coefficient based on a permutation approach; a heatmap is produced to visually represent the similarity matrix. Optionally, hierarchical agglomerative clustering can be performed and the silhouette method is used to identify an optimal number of clusters; the results of the clustering can be optionally used to sort the heatmap.
	"""
	
	cran = "brsim" 

	version("0.3", md5="d7317b3fc84b7712c466ea72a88b420d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cluster@2.1.4:", type=("build", "run"))
	depends_on("r-corrplot@0.92:", type=("build", "run"))
	depends_on("r-rcmdrmisc@2.7:", type=("build", "run"))
