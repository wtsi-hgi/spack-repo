# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJackstraw(RPackage):
	"""Statistical Inference for Unsupervised Learning

	Test for association between the observed data and their estimated latent variables. The jackstraw package provides a resampling strategy and testing scheme to estimate statistical significance of association between the observed data and their latent variables. Depending on the data type and the analysis aim, the latent variables may be estimated by principal component analysis (PCA), factor analysis (FA), K-means clustering, and related algorithms. The jackstraw methods learn over-fitting characteristics inherent in this circular analysis, where the observed data are used to estimate the latent variables and used again to test against that estimated latent variables. When latent variables are estimated by PCA, the jackstraw enables statistical testing for association between observed variables and latent variables, as estimated by low-dimensional principal components (PCs). This essentially leads to identifying variables that are significantly associated with PCs. Similarly, unsupervised clustering, such as K-means clustering, partition around medoids (PAM), and others, finds coherent groups in high-dimensional data. The jackstraw estimates statistical significance of cluster membership, by testing association between data and cluster centers. Clustering membership can be improved by using the resulting jackstraw p-values and posterior inclusion probabilities (PIPs), with an application to unsupervised evaluation of cell identities in single cell RNA-seq.
	"""
	
	cran = "jackstraw" 

	version("1.3.9", md5="e6bdd4c262ccaa25016ccceb055c93b7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
