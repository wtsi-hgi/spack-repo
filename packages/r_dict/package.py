# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDict(RPackage):
	"""R6 Based Key-Value Dictionary Implementation

	A key-value dictionary data structure based on R6 class which is designed to be similar usages with other languages dictionary (e.g. 'Python') with reference semantics and extendabilities by R6.
	"""
	
	homepage = "https://github.com/five-dots/Dict"
	cran = "Dict" 

	version("0.1.0", md5="3ead7a1d1b616c911bfcf108633ea81f")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
