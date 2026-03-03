# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalmodels(RPackage):
	"""Causal Inference Modeling for Estimation of Causal Effects

	
  Provides an array of statistical models common in causal inference such as 
  standardization, IP weighting, propensity matching, outcome regression, and doubly-robust 
  estimators. Estimates of the average treatment effects from each model are given with the 
  standard error and a 95% Wald confidence interval (Hernan, Robins (2020) <https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/>).
	"""
	
	homepage = "https://github.com/ander428/CausalModels"
	cran = "CausalModels" 

	version("0.2.0", md5="88a539bf742e331b1f056b69bd08579a")

	depends_on("r-causaldata", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
