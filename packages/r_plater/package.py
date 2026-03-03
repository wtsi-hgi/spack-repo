# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlater(RPackage):
	"""Read, Tidy, and Display Data from Microtiter Plates

	Tools for interacting with data from experiments done in microtiter
    plates. Easily read in plate-shaped data and convert it to tidy format, 
    combine plate-shaped data with tidy data, and view tidy data in plate shape.  
	"""
	
	homepage = "https://docs.ropensci.org/plater/"
	cran = "plater" 

	version("1.0.4", md5="96286c17790da073ae94bfdaedeb4469")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
