# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqueezy(RPackage):
	"""Group-Adaptive Elastic Net Penalised Generalised Linear Models

	Fit linear and logistic regression models penalised with group-adaptive elastic net penalties.
  The group penalties correspond to groups of covariates defined by a co-data group set.
  The method accommodates inclusion of unpenalised covariates and overlapping groups.
  See Van Nee et al. (2021) <arXiv:2101.03875>.
	"""
	
	homepage = "https://arxiv.org/abs/2101.03875"
	cran = "squeezy" 

	version("1.1-1", md5="00798be5b714e34b2f78618d2af20267")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-multiridge@1.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
