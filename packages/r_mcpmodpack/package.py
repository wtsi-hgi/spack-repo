# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcpmodpack(RPackage):
	"""Simulation-Based Design and Analysis of Dose-Finding Trials

	An efficient implementation of the MCPMod (Multiple Comparisons and Modeling) method to support a simulation-based design and analysis of dose-finding trials with normally distributed, binary and count endpoints (Bretz et al. (2005) <doi:10.1111/j.1541-0420.2005.00344.x>).
	"""
	
	homepage = "https://github.com/medianasoft/MCPModPack"
	cran = "MCPModPack" 

	version("0.5", md5="77d9fbf6d4e740ac9db809039a4bf118")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-devemf", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
