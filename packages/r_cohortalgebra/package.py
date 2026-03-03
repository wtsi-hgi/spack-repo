# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohortalgebra(RPackage):
	"""Use of Interval Algebra to Create New Cohort(s) from Existing
Cohorts

	This software tool is designed to generate new cohorts utilizing data from 
    previously instantiated cohorts. It employs interval algebra operators such as UNION, 
    INTERSECT, and MINUS to manipulate the data within the instantiated cohorts and 
    create new cohorts.
	"""
	
	homepage = "https://github.com/OHDSI/CohortAlgebra"
	cran = "CohortAlgebra" 

	version("0.2.0", md5="b5d82b9661dd37cfe5af84f60990e1b6")

	depends_on("r-databaseconnector@5:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sqlrender", type=("build", "run"))
