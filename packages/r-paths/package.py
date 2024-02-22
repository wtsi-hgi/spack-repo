# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaths(RPackage):
	"""An Imputation Approach to Estimating Path-Specific Causal
Effects

	In causal mediation analysis with multiple causally ordered mediators, a set of path-specific
  effects are identified under standard ignorability assumptions. This package implements an imputation
  approach to estimating these effects along with a set of bias formulas for conducting sensitivity analysis
  (Zhou and Yamamoto <doi:10.31235/osf.io/2rx6p>). It contains two main functions: paths() for estimating 
  path-specific effects and sens() for conducting sensitivity analysis. Estimation uncertainty is quantified 
  using the nonparametric bootstrap.
	"""
	
	cran = "paths" 

	version("0.1.1", md5="8e2e0e5a6c1f7cb9e8deed5f6efc041c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bart", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
