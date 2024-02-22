# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsweight(RPackage):
	"""Propensity Score Weighting for Causal Inference with
Observational Studies and Randomized Trials

	Supports propensity score weighting analysis of observational studies and randomized trials. Enables the estimation and inference of average causal effects with binary and multiple treatments using overlap weights (ATO), inverse probability of treatment weights (ATE), average treatment effect among the treated weights (ATT), matching weights (ATM) and entropy weights (ATEN), with and without propensity score trimming. These weights are members of the family of balancing weights introduced in Li, Morgan and Zaslavsky (2018) <doi:10.1080/01621459.2016.1260466> and Li and Li (2019) <doi:10.1214/19-AOAS1282>.
	"""
	
	homepage = "https://github.com/thuizhou/PSweight"
	cran = "PSweight" 

	version("1.1.8", md5="a77ba912fd2375c6f12e1da61d732be2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
