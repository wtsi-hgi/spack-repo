# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebugr(RPackage):
	"""Debug Tool to Watch Objects/Expressions While Running an R
Script

	Tool to print out the value of R objects/expressions while running
  an R script. Outputs can be made dependent on user-defined conditions/criteria. 
  Debug messages only appear when a global option for debugging is set. 
  This way, 'debugr' code can even remain in the debugged code for later use 
  without any negative effects during normal runtime.
	"""
	
	homepage = "https://github.com/jsugarelli/debugr/"
	cran = "debugr" 

	version("0.0.1", md5="64e1548bf595ad7f50df71e48353f81a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
