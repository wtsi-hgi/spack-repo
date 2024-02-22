# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossnma(RPackage):
	"""Cross-Design & Cross-Format Network Meta-Analysis and Regression

	Network meta-analysis and meta-regression (allows
  including up to three covariates) for individual participant data,
  aggregate data, and mixtures of both formats using the three-level
  hierarchical model.  Each format can come from randomized controlled
  trials or non-randomized studies or mixtures of both. Estimates are
  generated in a Bayesian framework using JAGS. The implemented models
  are described by Hamza et al. 2023 <DOI:10.1002/jrsm.1619>.
	"""
	
	homepage = "https://github.com/htx-r/crossnma"
	cran = "crossnma" 

	version("1.2.0", md5="5e0fa3ea41d640404a95b91731d3fdef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
	depends_on("r-netmeta@2.8.0:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
