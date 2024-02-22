# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSportscausal(RPackage):
	"""Spillover Time Series Causal Inference

	A time series causal inference model for Randomized Controlled Trial (RCT) under spillover effect. 'SPORTSCausal' (Spillover Time Series Causal Inference) separates treatment effect and spillover effect from given responses of experiment group and control group by predicting the response without treatment. It reports both effects by fitting the Bayesian Structural Time Series (BSTS) model based on 'CausalImpact', as described in Brodersen et al. (2015) <doi:10.1214/14-AOAS788>. 
	"""
	
	cran = "SPORTSCausal" 

	version("1.0", md5="2cb69cc9c16fffec4b218ee544afa0f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-causalimpact", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
