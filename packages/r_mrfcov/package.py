# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrfcov(RPackage):
	"""Markov Random Fields with Additional Covariates

	Approximate node interaction parameters of Markov Random Fields 
    graphical networks. Models can incorporate additional covariates, allowing users to estimate
    how interactions between nodes in the graph are predicted to change across
    covariate gradients. The general methods implemented in this package are described 
    in Clark et al. (2018) <doi:10.1002/ecy.2221>.
	"""
	
	homepage = "https://github.com/nicholasjclark/MRFcov"
	cran = "MRFcov" 

	version("1.0.39", md5="6ebc67c94e8a60d567b3ef65050e383c")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
