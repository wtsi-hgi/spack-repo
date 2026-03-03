# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnglercreelsurveysimulation(RPackage):
	"""Simulate a Bus Route Creel Survey of Anglers

	Simulate an angler population, sample the simulated population with a user-specified survey times, and calculate metrics from a bus route-type creel survey.
	"""
	
	cran = "AnglerCreelSurveySimulation" 

	version("1.0.2", md5="50099927753023d58c20db6465ffb921")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
