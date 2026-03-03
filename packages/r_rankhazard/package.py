# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankhazard(RPackage):
	"""Rank-Hazard Plots

	Rank-hazard plots Karvanen and Harrell (2009) <DOI:10.1002/sim.3591> visualize the relative importance of covariates in a proportional hazards model. The key idea is to rank the covariate values and plot the relative hazard as a function of ranks scaled to interval [0,1]. The relative hazard is plotted in respect to the reference hazard, which can bee.g. the hazard related to the median of the covariate.
	"""
	
	cran = "rankhazard" 

	version("1.1.0", md5="419b116db9bfb5f825974efc217e90ad")

	depends_on("r-survival", type=("build", "run"))
