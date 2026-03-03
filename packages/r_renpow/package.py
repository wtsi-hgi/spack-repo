# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRenpow(RPackage):
	"""Renewable Power Systems and the Environment

	Supports calculations and visualization for renewable power systems and the environment. Analysis and graphical tools for DC and AC circuits and their use in electric power systems. Analysis and graphical tools for thermodynamic cycles and heat engines, supporting efficiency calculations in coal-fired power plants, gas-fired power plants. Calculations of carbon emissions and atmospheric CO2 dynamics. Analysis of power flow and demand for the grid, as well as power models for microgrids and off-grid systems. Provides resource and power generation for hydro power, wind power, and solar power.    
	"""
	
	homepage = "https://www.r-project.org/"
	cran = "renpow" 

	version("0.1-1", md5="9083487e756e745bd8319ebc0e11eff0")

	depends_on("r@2.10:", type=("build", "run"))
