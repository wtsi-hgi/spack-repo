# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpcerf(RPackage):
	"""Gaussian Processes for Estimating Causal Exposure Response
Curves

	Provides a non-parametric Bayesian framework based on Gaussian process priors for estimating causal effects of a continuous exposure and detecting change points in the causal exposure response curves using observational data. Ren, B., Wu, X., Braun, D., Pillai, N., & Dominici, F.(2021). "Bayesian modeling for exposure response curve via gaussian processes: Causal effects of exposure to air pollution on health outcomes." arXiv preprint <arXiv:2105.03454>.
	"""
	
	homepage = "https://github.com/NSAPH-Software/GPCERF"
	cran = "GPCERF" 

	version("0.2.3", md5="624f728a3802037aaf7910d55956f31a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-wcorr", type=("build", "run"))
