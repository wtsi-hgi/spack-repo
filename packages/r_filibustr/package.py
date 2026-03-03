# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilibustr(RPackage):
	"""Data Utilities for Congressional Research

	Provides easy-to-understand and consistent interfaces for accessing data on the U.S. Congress. 
    The functions in 'filibustr' streamline the process for importing data on Congress into R, 
    removing the need to download and work from CSV files and the like. 
    Data sources include 'Voteview' (<https://voteview.com/>), the U.S. Senate website (<https://www.senate.gov/>), and more.
	"""
	
	homepage = "https://github.com/feinleib/filibustr"
	cran = "filibustr" 

	version("0.2.0", md5="050c4f5eac4e6572d7f4c20c2065907c")
	version("0.1.1", md5="4e2820f5a9dab791b2a71cbc2242d0c1")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
