# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhase12compare(RPackage):
	"""Simulates SPSO and Efftox Phase 12 Trials with Correlated
Outcomes

	Simulating and conducting four phase 12 clinical trials with correlated binary bivariate outcomes described. Uses the 'Efftox' (efficacy and toxicity tradeoff, <https://biostatistics.mdanderson.org/SoftwareDownload/SingleSoftware/Index/2>) and SPSO (Semi-Parametric Stochastic Ordering) models with Utility and Desirability based objective functions for dose finding. 
	"""
	
	cran = "Phase12Compare" 

	version("1.5", md5="4adbdb867c29e3fb5d1e0879bf27b942")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
