# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilevel(RPackage):
	"""Multilevel Functions

	Tools used by organizational researchers for the analysis of multilevel data. Includes four broad sets of tools. First, functions for estimating within-group agreement and reliability indices. Second, functions for manipulating multilevel and longitudinal (panel) data. Third, simulations for estimating power and generating multilevel data. Fourth, miscellaneous functions for estimating reliability and performing simple calculations and data transformations.  
	"""
	
	homepage = "https://www.r-project.org"
	cran = "multilevel" 

	version("2.7", md5="866b05a102045cbdba5c4acb778f44d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
