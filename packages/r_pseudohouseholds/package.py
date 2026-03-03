# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPseudohouseholds(RPackage):
	"""Generate Pseudohouseholds on Road Networks in Regions

	Given an arbitrary set of spatial regions and road networks, 
             generate a set of representative points, or pseudohouseholds, that
             can be used for travel burden analysis. Parallel processing is 
             supported.
	"""
	
	homepage = "https://github.com/chris31415926535/pseudohouseholds"
	cran = "pseudohouseholds" 

	version("0.1.1", md5="f525885da6c232f81fdfeff74eb8d141")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
