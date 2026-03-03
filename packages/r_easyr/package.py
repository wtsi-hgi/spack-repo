# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyr(RPackage):
	"""Helpful Functions from Oliver Wyman Actuarial Consulting

	Makes difficult operations easy. Includes these types of functions: 
    shorthand, type conversion, data wrangling, and work flow. 
    Also includes some helpful data objects: NA strings, U.S. state list, color blind charting colors. 
    Built and shared by Oliver Wyman Actuarial Consulting. Accepting proposed contributions through GitHub.
	"""
	
	homepage = "https://github.com/oliver-wyman-actuarial/easyr"
	cran = "easyr" 

	version("0.5-11", md5="9756efd3678e83c6da566e684f498115")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
