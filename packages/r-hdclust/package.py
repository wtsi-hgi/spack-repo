# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdclust(RPackage):
	"""Clustering High Dimensional Data with Hidden Markov Model on
Variable Blocks

	Clustering of high dimensional data with Hidden Markov Model on Variable Blocks (HMM-VB) fitted via Baum-Welch algorithm. Clustering is performed by the Modal Baum-Welch algorithm (MBW), which finds modes of the density function. Lin Lin and Jia Li (2017) <http://jmlr.org/papers/v18/16-342.html>.
	"""
	
	cran = "HDclust" 

	version("1.0.3", md5="c9061b8c17e047d5b8dda5894ad5d001")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rtsne@0.11:", type=("build", "run"))
