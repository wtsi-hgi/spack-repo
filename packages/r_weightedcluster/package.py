# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedcluster(RPackage):
	"""Clustering of Weighted Data

	Clusters state sequences and weighted data. It provides an optimized weighted PAM algorithm as well as functions for aggregating replicated cases, computing cluster quality measures for a range of clustering solutions and plotting (fuzzy) clusters of state sequences. Parametric bootstraps methods to validate typology of sequences are also provided.
	"""
	
	homepage = "http://mephisto.unige.ch/weightedcluster/"
	cran = "WeightedCluster" 

	version("1.6-4", md5="e327bf3eabed393715c0792779a9a9dd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-traminer@2.0.6:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
