# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmvbvs(RPackage):
	"""Missing Multivariate Bayesian Variable Selection

	A variable selection tool for multivariate normal variables with missing-at-random values using Bayesian Hierarchical Model.
    Visualization functions show the posterior distribution of gamma (inclusion variables) and beta (coefficients). 
    Users can also visualize the heatmap of the posterior mean of covariance matrix. 
    Kim, T. Nicolae, D. (2019) <https://github.com/tk382/MMVBVS/blob/master/workingpaper.pdf>.
    Guan, Y. Stephens, M. (2011) <doi:10.1214/11-AOAS455>.
	"""
	
	cran = "MMVBVS" 

	version("0.8.0", md5="b494822e2cba12bf3477cf1a0f6e1c44")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
