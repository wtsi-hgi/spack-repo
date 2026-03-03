# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCongress(RPackage):
	"""Access the Congress.gov API

	Download and read data on United States congressional proceedings. 
    Data is read from the Library of Congress's Congress.gov Application Programming 
    Interface (<https://github.com/LibraryOfCongress/api.congress.gov/>). Functions
    exist for all version 3 endpoints, including for bills, amendments, congresses, 
    summaries, members, reports, communications, nominations, and treaties.
	"""
	
	homepage = "https://github.com/christopherkenny/congress"
	cran = "congress" 

	version("0.0.3", md5="ecfcc1a7feeb3dd5787adf7a6b98d9bb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
