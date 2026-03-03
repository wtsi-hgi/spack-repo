# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHclust1d(RPackage):
	"""Hierarchical Clustering of Univariate (1d) Data

	Univariate agglomerative hierarchical clustering with a comprehensive list of choices of a linkage function in O(n*log n) time. The better algorithmic time complexity is paired with an efficient 'C++' implementation.
	"""
	
	homepage = "https://github.com/SzymonNowakowski/hclust1d"
	cran = "hclust1d" 

	version("0.1.1", md5="ac32d8a28c77159210055e2c47ff5363")

	depends_on("r-rcpp", type=("build", "run"))
