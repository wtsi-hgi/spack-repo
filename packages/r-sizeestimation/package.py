# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSizeestimation(RPackage):
	"""Estimating the Sizes of Populations at Risk of HIV Infection
from Multiple Data Sources Using a Bayesian Hierarchical Model

	This function develops an algorithm for presenting a Bayesian hierarchical model for estimating the sizes of local and national drug injected populations in Bangladesh. The model incorporates multiple commonly used data sources including mapping data, surveys, interventions, capture-recapture data, estimates or guesstimates from organizations, and expert opinion.
	"""
	
	cran = "SizeEstimation" 

	version("1.1.1", md5="1c6b0debace71a0628c4b9cc62323ecd")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
