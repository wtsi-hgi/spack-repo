# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivar(RPackage):
	"""Penalized Estimation of Multiple-Subject Vector Autoregressive
(multi-VAR) Models

	Functions for simulating, estimating and forecasting stationary Vector Autoregressive (VAR) models for multiple subject data using the penalized multi-VAR framework in Fisher, Kim and Pipiras (2020) <arXiv:2007.05052>. 
	"""
	
	cran = "multivar" 

	version("1.1.0", md5="23f7e9093f3e8ad213e84386caeca62b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
