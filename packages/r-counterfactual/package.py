# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCounterfactual(RPackage):
	"""Estimation and Inference Methods for Counterfactual Analysis

	Implements the estimation and inference methods for counterfactual analysis described in Chernozhukov, Fernandez-Val and Melly (2013) <DOI:10.3982/ECTA10582> "Inference on Counterfactual Distributions," Econometrica, 81(6). The counterfactual distributions considered are the result of changing either the marginal distribution of covariates related to the outcome variable of interest, or the conditional distribution of the outcome given the covariates. They can be applied to estimate quantile treatment effects and wage decompositions.
	"""
	
	cran = "Counterfactual" 

	version("1.2", md5="8c38fe6b769da8ba2b0224d859b59c85")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
