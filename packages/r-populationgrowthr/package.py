# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopulationgrowthr(RPackage):
	"""Linear Population Growth Scenarios

	Fit linear splines to species time series to detect population growth scenarios based on Hyndman, R J and Mesgaran, M B and Cousens, R D (2015) <doi:10.1007/s10530-015-0962-8>.
	"""
	
	cran = "PopulationGrowthR" 

	version("0.1.1", md5="fa3e0a6df7a2e83a0bc3336887995447")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
