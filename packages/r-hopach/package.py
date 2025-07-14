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

	version("2.68.0", commit="cff618aa7a4fd79ddc7ecee571ac7819882b8b0c")
	version("2.62.0", commit="f0c6ddc9bf7fe20a412cb9e330a8aadf0fb9523b")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
