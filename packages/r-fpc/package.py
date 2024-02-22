# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpc(RPackage):
	"""Flexible Procedures for Clustering.

	Various methods for clustering and cluster validation. Fixed point
	clustering. Linear regression clustering. Clustering by  merging Gaussian
	mixture components. Symmetric  and asymmetric discriminant projections for
	visualisation of the  separation of groupings. Cluster validation
	statistics for distance based clustering including corrected Rand index.
	Standardisation of cluster validation statistics by random clusterings and
	comparison between many clustering methods and numbers of clusters based on
	this.   Cluster-wise cluster stability assessment. Methods for estimation
	of  the number of clusters: Calinski-Harabasz, Tibshirani and Walther's
	prediction strength, Fang and Wang's bootstrap stability.
	Gaussian/multinomial mixture fitting for mixed  continuous/categorical
	variables. Variable-wise statistics for cluster interpretation. DBSCAN
	clustering. Interface functions for many  clustering methods implemented in
	R, including estimating the number of clusters with kmeans, pam and clara.
	Modality diagnosis for Gaussian mixtures. For an overview see
	package?fpc."""

	cran = "fpc"

	version("2.2-11", md5="8d1a3172c2ee3e1d7bf8e73b753482ad")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-prabclus", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
