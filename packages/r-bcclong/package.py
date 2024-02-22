# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcclong(RPackage):
	"""Bayesian Consensus Clustering for Multiple Longitudinal Features

	It is very common nowadays for a study to collect multiple
    features and appropriately integrating multiple longitudinal features
    simultaneously for defining individual clusters becomes increasingly
    crucial to understanding population heterogeneity and predicting
    future outcomes.  'BCClong' implements a Bayesian consensus clustering
    (BCC) model for multiple longitudinal features via a generalized
    linear mixed model. Compared to existing packages, several key
    features make the 'BCClong' package appealing: (a) it allows
    simultaneous clustering of mixed-type (e.g., continuous, discrete and
    categorical) longitudinal features, (b) it allows each longitudinal
    feature to be collected from different sources with measurements taken
    at distinct sets of time points (known as irregularly sampled
    longitudinal data), (c) it relaxes the assumption that all features
    have the same clustering structure by estimating the feature-specific
    (local) clusterings and consensus (global) clustering.
	"""
	
	cran = "BCClong" 

	version("1.0.2", md5="a0fc3aaa360b833d87aae8d178581a00")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-label-switching", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mixak", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
