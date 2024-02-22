# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperiences(RPackage):
	"""Experience Research

	Provides convenience functions for researching experiences 
    including user, customer, patient, employee, and other human experiences.
    It provides a suite of tools to simplify data exploration such as 
    benchmarking, comparing groups, and checking for differences. The outputs 
    translate statistical approaches in applied experience research to 
    human readable output. 
	"""
	
	cran = "experiences" 

	version("0.1.1", md5="c288f58d41cc2e0ba44cc1deb4623f01")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-huxtable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
