# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpeds(RPackage):
	"""Data from the Integrated Post-Secondary Education Data System

	Contains data on Post-Secondary Institution Statistics in 2020 <https://nces.ed.gov/ipeds/use-the-data>. The package allows easy access to a wide variety of information regarding Post-secondary Institutions, its students, faculty, and their demographics, financial aid, educational and recreational offerings, and completions. This package can be used by students, college counselors, or involved parents interested in pursuing higher education, considering their options, and securing admission into their school of choice.
	"""
	
	cran = "IPEDS" 

	version("0.1.0", md5="1ec8d0ed5a7e3452547bea8c88479bf7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
