# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvsens(RPackage):
	"""Sensitivity Analysis with Time-to-Event Outcomes

	Performs a dual-parameter sensitivity analysis of treatment effect to unmeasured confounding in observational studies with either survival or competing risks outcomes. Huang, R., Xu, R. and Dulai, P.S.(2020) <doi:10.1002/sim.8672>.
	"""
	
	homepage = "https://github.com/Rong0707/survSens"
	cran = "survSens" 

	version("1.1.0", md5="b2686213cfe8edbb61efc44c057efbe6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
