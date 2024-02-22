# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocnp(RPackage):
	"""Work with Romanian Personal Numeric Codes PNC / CNP

	A set of tools for working with Romanian personal numeric codes. 
    The core is a validation function which applies several verification
    criteria to assess the validity of numeric codes. This is accompanied by 
    functionality for extracting the different components of a personal numeric
    code. A personal numeric code is issued to all Romanian residents either at 
    birth or when they obtain a residence permit.
	"""
	
	homepage = "https://github.com/dragosmg/rocnp"
	cran = "rocnp" 

	version("0.1.0", md5="8832ce7867ce9023adb9859c07ae8953")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
