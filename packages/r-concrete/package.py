# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcrete(RPackage):
	"""Continuous-Time Competing Risks Estimation using Targeted
Minimum Loss-Based Estimation (TMLE)

	One-step continuous-time Targeted Minimum Loss-Based Estimation (TMLE) for outcome-specific absolute risk estimands in right-censored survival settings with or without competing risks, implementing the methodology described in Rytgaard et al. (2023) <doi:10.1111/biom.13856> and Rytgaard and van der Laan (2023) <doi:10.1007/s10985-022-09576-2>. Currently 'concrete' can be used to estimate the effects of static or dynamic interventions on binary treatments given at baseline, cross-validated initial estimation of treatment propensity is done using the 'SuperLearner' package, and initial estimation of conditional hazards is done using ensembles of Cox regressions from the 'survival' package or Coxnet from the 'glmnet' package.
	"""
	
	homepage = "https://github.com/imbroglio-dc/concrete"
	cran = "concrete" 

	version("1.0.5", md5="31f0648c8228b29a4cc8d39ed541d730")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-origami", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
