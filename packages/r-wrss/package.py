# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrss(RPackage):
	"""Water Resources System Simulator

	Water resources system simulator is a tool for simulation and analysis of large-scale water resources systems. 'WRSS' proposes functions and methods for construction, simulation and analysis of primary storage and hydropower water resources features (e.g. reservoirs, aquifers, and etc.) based on Standard Operating Policy (SOP). 
	"""
	
	cran = "WRSS" 

	version("3.1", md5="575cd0a9ee4ee8841a3a7c90883a4e82")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
