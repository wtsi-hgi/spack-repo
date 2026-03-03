# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustimpute(RPackage):
	"""K-Means Clustering with Build-in Missing Data Imputation

	This k-means algorithm is able to cluster data with missing values and as a by-product completes the data set. The implementation can deal with missing values in multiple variables and is computationally efficient since it iteratively uses the current cluster assignment to define a plausible distribution for missing value imputation. Weights are used to shrink early random draws for missing values (i.e., draws based on the cluster assignments after few iterations) towards the global mean of each feature. This shrinkage slowly fades out after a fixed number of iterations to reflect the increasing credibility of cluster assignments. See the vignette for details.
	"""
	
	cran = "ClustImpute" 

	version("0.2.4", md5="87859db75300e6a76fded1e34e068da6")

	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
