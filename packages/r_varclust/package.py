# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarclust(RPackage):
	"""Variables Clustering

	Performs clustering of quantitative variables,
    assuming that clusters lie in low-dimensional subspaces. Segmentation of
    variables, number of clusters and their dimensions are selected based on
    BIC. Candidate models are identified based on many runs of K-means
    algorithm with different random initializations of cluster centers.
	"""
	
	cran = "varclust" 

	version("0.9.4", md5="39b83795f2a98b735ca1ecd4c67db0dd")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-pesel", type=("build", "run"))
