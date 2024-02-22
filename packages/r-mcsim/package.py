# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcsim(RPackage):
	"""Determine the Optimal Number of Clusters

	Identifies the optimal number of clusters by calculating the similarity between
             two clustering methods at the same number of clusters using the corrected indices of Rand and
             Jaccard as described in Albatineh and Niewiadomska-Bugaj (2011). The number of clusters at
             which the index attain its maximum more frequently is a candidate for being the optimal
             number of clusters.
	"""
	
	cran = "MCSim" 

	version("1.0", md5="f888f4a475b0d90470be645a86765e3e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
