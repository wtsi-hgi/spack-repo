# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsirm12pl(RPackage):
	"""Latent Space Item Response Model

	Analysis of dichotomous and continuous response data using latent factor by both 1PL LSIRM and 2PL LSIRM as described in Jeon et al. (2021) <doi:10.1007/s11336-021-09762-5>. It includes original 1PL LSIRM and 2PL LSIRM provided for binary response data and its extension for continuous response data. Bayesian model selection with spike-and-slab prior and method for dealing data with missing value under missing at random, missing completely at random are also supported. Various diagnostic plots are available to inspect the latent space and summary of estimated parameters.
	"""
	
	cran = "lsirm12pl" 

	version("1.3.1", md5="33dec6a9508d0ddff557a2d2530669d7")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-spatstat", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
