# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDevfunc(RPackage):
	"""Clear and Condense Argument Check for User-Defined Functions

	A concise check of the format of one or multiple input arguments (data type, length or value) is provided. Since multiple input arguments can be tested simultaneously, a lengthly list of checks at the beginning of your function can be avoided, hereby enhancing the readability and maintainability of your code.
	"""
	
	cran = "devFunc" 

	version("0.1", md5="657c87abdea50aeeac1effa5d9c8f135")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-stringr@1.1:", type=("build", "run"))
