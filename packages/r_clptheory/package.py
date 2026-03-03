# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClptheory(RPackage):
	"""Compute Price of Production and Labor Values

	Computes the uniform rate of profit, the vector of price of 
    production and the vector of labor values; and also compute measures of deviation 
    between relative prices of production and relative values.  
    <https://scholarworks.umass.edu/econ_workingpaper/347/>. You provide the  
    input-output data and 'clptheory' does the calculations for you.
	"""
	
	homepage = "https://github.com/dbasu-umass/clptheory/"
	cran = "clptheory" 

	version("0.1.0", md5="2711d60a4586009842318632d8f47ec8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-popdemo", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
