# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwoarmsurvsim(RPackage):
	"""Simulate Survival Data for Randomized Clinical Trials

	A system to simulate clinical trials with time to event endpoints. Event simulation is based on Cox models allowing for covariates in addition to the treatment or group factor. Specific drop-out rates (separate from administrative censoring) can be controlled in the simulation. Other features include stratified randomization, non-proportional hazards, different accrual patterns, and event projection (timing to reach the target event) based on interim data.
	"""
	
	cran = "TwoArmSurvSim" 

	version("0.2", md5="787c3f8cfb5cf30851d1b42c5284ab4b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-blockrand", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-simsurv", type=("build", "run"))
