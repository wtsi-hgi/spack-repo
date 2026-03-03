# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpdclustering(RPackage):
	"""PD-Clustering and Related Methods

	Probabilistic distance clustering (PD-clustering) is an iterative, distribution free, probabilistic clustering method. PD-clustering assigns units to a cluster according to their probability of membership, under the constraint that the product of the probability and the distance of each point to any cluster centre is a constant. PD-clustering is a flexible method that can be used with non-spherical clusters, outliers, or noisy data. PDQ is an extension of the algorithm for clusters of different size. GPDC and TPDC uses a dissimilarity measure based on densities. Factor PD-clustering (FPDC) is a factor clustering method that involves a linear transformation of variables and a cluster optimizing the PD-clustering criterion. It works on high dimensional data sets.
	"""
	
	cran = "FPDclustering" 

	version("2.3.1", md5="3aaec74d6108013a16051381f39e66cb")

	depends_on("r-threeway", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-exposition", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-klar", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggeasy", type=("build", "run"))
