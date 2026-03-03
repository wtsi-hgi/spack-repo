# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasecohortcoxsurvival(RPackage):
	"""Case-Cohort Cox Survival Inference

	Cox model inference for relative hazard and covariate-specific pure risk estimated 
             from stratified and unstratified case-cohort data as described in 
             Etievant, L., Gail, M.H. (2023) <arXiv:2304.03396>.
	"""
	
	cran = "CaseCohortCoxSurvival" 

	version("0.0.34", md5="150d879861ea59770bafd1bbd5346160")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
