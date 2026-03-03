# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvauditor(RPackage):
	"""Creates Assertion Tests

	Offers a comprehensive set of assertion tests to help users validate the integrity of their data. 
    These tests can be used to check for specific conditions or properties within a dataset and 
    help ensure that data is accurate and reliable. 
    The package is designed to make it easy to add quality control checks to data analysis 
    workflows and to aid in identifying and correcting any errors or inconsistencies in data.
	"""
	
	cran = "vvauditor" 

	version("0.6.0", md5="7e6c0f6412bb3cbc6c6603bcc7b857ff")
	version("0.5.8", md5="4702194c3cd673b47ec8057f6fba5ddc")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-findr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-kit", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
