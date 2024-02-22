# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBikm1(RPackage):
	"""Co-Clustering Adjusted Rand Index and Bikm1 Procedure for
Contingency and Binary Data-Sets

	Co-clustering of the rows and columns of a contingency or binary matrix, or double binary matrices and model selection for the number of row and column clusters. Three models are considered: the Poisson latent block model for contingency matrix, the binary latent block model for binary matrix and a new model we develop: the multiple latent block model for double binary matrices. A new procedure named bikm1 is implemented to investigate more efficiently the grid of numbers of clusters. Then, the studied model selection criteria are the integrated completed likelihood (ICL) and the Bayesian integrated likelihood (BIC). Finally, the co-clustering adjusted Rand index (CARI) to measure agreement between co-clustering partitions is implemented. Robert Valerie, Vasseur Yann, Brault Vincent (2021) <doi:10.1007/s00357-020-09379-w>.
	"""
	
	cran = "bikm1" 

	version("1.1.0", md5="3e7d35991f4ff9ecd8bfa99802ae4042", url="https://cran.r-project.org/src/contrib/bikm1_1.1.0.tar.gz")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
