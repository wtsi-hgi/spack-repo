# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhms(RPackage):
	"""Hydrologic Modelling System for R Users

	Hydrologic modelling system is an object oriented tool for simulation and analysis of hydrologic events. The package proposes functions and methods for construction, simulation, visualization, and calibration of a hydrologic model.
	"""
	
	cran = "RHMS" 

	version("1.7", md5="5a41f9b21583838f75aef53d6afeb7eb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
