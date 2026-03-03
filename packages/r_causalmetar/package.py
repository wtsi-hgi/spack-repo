# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalmetar(RPackage):
	"""Causally Interpretable Meta-Analysis

	Provides robust and efficient methods for estimating causal effects in a target population using a multi-source dataset, including those of Dahabreh et al. (2019) <doi:10.1111/biom.13716> and Robertson et al. (2021) <arXiv:2104.05905>. The multi-source data can be a collection of trials, observational studies, or a combination of both, which have the same data structure (outcome, treatment, and covariates). The target population can be based on an internal dataset or an external dataset where only covariate information is available. The causal estimands available are average treatment effects and subgroup treatment effects.  
	"""
	
	homepage = "https://github.com/ly129/CausalMetaR"
	cran = "CausalMetaR" 

	version("0.1.1", md5="9d9eca49d843d3a9fe0a21265a352fc9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
