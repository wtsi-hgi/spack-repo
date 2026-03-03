# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarlasso(RPackage):
	"""Conditional Autoregressive LASSO

	Algorithms to fit Bayesian Conditional Autoregressive LASSO with automatic and adaptive shrinkage described in Shen and Solis-Lemus (2020) <arXiv:2012.08397>.
	"""
	
	homepage = "https://github.com/YunyiShen/CAR-LASSO"
	cran = "CARlasso" 

	version("0.1.2", md5="d3f0faad9d4d6d323d1f6ecd25b9c91f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
