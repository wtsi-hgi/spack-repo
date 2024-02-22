# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarecall(RPackage):
	"""Government of Canada Vehicle Recalls Database API Wrapper

	Provides API access to the Government of Canada Vehicle Recalls 
    Database <https://tc.api.canada.ca/en/detail?api=VRDB> used by the Defect 
    Investigations and Recalls Division for vehicles, tires, and child car 
    seats. The API wrapper provides access to recall summary information 
    searched using make, model, and year range, as well as detailed recall 
    information searched using recall number.
	"""
	
	homepage = "https://github.com/WraySmith/caRecall"
	cran = "caRecall" 

	version("0.1.0", md5="35d6d98821d2944c900582ea72984894")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
