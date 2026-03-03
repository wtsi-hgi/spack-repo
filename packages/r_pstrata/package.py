# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPstrata(RPackage):
	"""Principal Stratification Analysis in R

	Estimating causal effects in the presence of post-treatment confounding using principal stratification. 'PStrata' allows for customized monotonicity assumptions and exclusion restriction assumptions, with automatic full Bayesian inference supported by 'Stan'. The main function to use in this package is PStrata(), which provides posterior estimates of principal causal effect with uncertainty quantification. Visualization tools are also provided for diagnosis and interpretation. See Liu and Li (2023) <arXiv:2304.02740> for details.
	"""
	
	cran = "PStrata" 

	version("0.0.5", md5="9fa0356aa9b84354ddb2318e7471dc58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
