# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcpmod(RPackage):
	"""Design and Analysis of Dose-Finding Studies

	Implements a methodology for the design and analysis of dose-response studies that
             combines aspects of multiple comparison procedures  and modeling approaches
	     (Bretz, Pinheiro and Branson, 2005, Biometrics 61, 738-748, <doi: 10.1111/j.1541-0420.2005.00344.x>).
             The package provides tools for the analysis of dose finding trials as well as a variety
             of tools necessary to plan a trial to be conducted with the MCP-Mod methodology.
             Please note: The 'MCPMod' package will not be further developed, all future development of 
             the MCP-Mod methodology will be done in the 'DoseFinding' R-package. 
	"""
	
	cran = "MCPMod" 

	version("1.0-10.1", md5="1e25a4818f39bf9133182cae090a9b1d")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r@2.4.1:", type=("build", "run"))
