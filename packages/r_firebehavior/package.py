# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFirebehavior(RPackage):
	"""Prediction of Wildland Fire Behavior and Hazard

	Fire behavior prediction models, including the Scott & Reinhardt's (2001) Rothermel Wildland Fire Modelling System <DOI:10.2737/RMRS-RP-29> and Alexander et al.'s (2006) Crown Fire Initiation & Spread model <DOI:10.1016/j.foreco.2006.08.174>. Also contains sample datasets, estimation of fire behavior prediction model inputs (e.g., fuel moisture, canopy characteristics, wind adjustment factor), results visualization, and methods to estimate fire weather hazard.
	"""
	
	cran = "firebehavioR" 

	version("0.1.2", md5="0fd3de458e4a5e93a73a5a2f5a7cca57")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
