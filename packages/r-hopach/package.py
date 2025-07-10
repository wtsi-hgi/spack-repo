# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHopach(RPackage):
	"""Hierarchical Ordered Partitioning and Collapsing Hybrid (HOPACH)

	The HOPACH clustering algorithm builds a hierarchical tree of clusters by recursively partitioning a data set, while ordering and possibly collapsing clusters at each level. The algorithm uses the Mean/Median Split Silhouette (MSS) criteria to identify the level of the tree with maximally homogeneous clusters. It also runs the tree down to produce a final ordered list of the elements. The non-parametric bootstrap allows one to estimate the probability that each element belongs to each cluster (fuzzy clustering).
	"""
	
	homepage = "http://www.stat.berkeley.edu/~laan/"
	bioc = "hopach" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hopach_2.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hopach/hopach_2.62.0.tar.gz"]

	version("2.62.0", sha256="9a84cf8bdb414ec7a188ee4c4bb4ceed9a47ef6d0534ecabd2889e72cec419ec")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
