# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomforestsrc(RPackage):
	"""Fast Unified Random Forests for Survival, Regression, and
Classification (RF-SRC)

	Fast OpenMP parallel computing of Breiman's random forests for univariate, multivariate, unsupervised, survival, competing risks, class imbalanced classification and quantile regression. New Mahalanobis splitting for correlated outcomes.  Extreme random forests and randomized splitting.  Suite of imputation methods for missing data.  Fast random forests using subsampling. Confidence regions and standard errors for variable importance. New improved holdout importance. Case-specific importance.  Minimal depth variable importance. Visualize trees on your Safari or Google Chrome browser. Anonymous random forests for data privacy.
	"""
	
	homepage = "https://www.randomforestsrc.org/"
	cran = "randomForestSRC" 

	version("3.2.3", md5="8de4d9d11d01ecfcde4c7ab30c686394")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
