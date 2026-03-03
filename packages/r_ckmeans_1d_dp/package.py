# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCkmeans1dDp(RPackage):
	"""Optimal, Fast, and Reproducible Univariate Clustering

	Fast, optimal, and reproducible weighted univariate
 clustering by dynamic programming. Four problems are solved, including
 univariate k-means (Wang & Song 2011) <doi:10.32614/RJ-2011-015>
 (Song & Zhong 2020) <doi:10.1093/bioinformatics/btaa613>, k-median,
 k-segments, and multi-channel weighted k-means. Dynamic programming
 is used to minimize the sum of (weighted) within-cluster distances
 using respective metrics. Its advantage over heuristic clustering in
 efficiency and accuracy is pronounced when there are many clusters.
 Multi-channel weighted k-means groups multiple univariate
 signals into k clusters. An auxiliary function generates histograms
 adaptive to patterns in data. This package provides a powerful set
 of tools for univariate data analysis with guaranteed optimality,
 efficiency, and reproducibility, useful for peak calling on temporal,
 spatial, and spectral data.
	"""
	
	cran = "Ckmeans.1d.dp" 

	version("4.3.5", md5="6bfe2e4648c48a5af5565954c71dca13")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.6.1:", type=("build", "run"))
