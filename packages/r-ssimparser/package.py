# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsimparser(RPackage):
	"""Standard Schedules Information Parser

	Parse Standard Schedules Information file (types 2 and 3) into a Data Frame.
    Can also expand schedules into flights.
	"""
	
	cran = "ssimparser" 

	version("0.1.1", md5="9f383ab0a5ddfe57c2e80869229a0e65")

	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-airportr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
