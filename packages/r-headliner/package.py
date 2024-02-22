# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeadliner(RPackage):
	"""Compose Sentences to Describe Comparisons

	Create dynamic, data-driven text. Given two values, a list of 
    talking points is generated and can be combined using string
    interpolation. Based on the 'glue' package.
	"""
	
	homepage = "https://rjake.github.io/headliner/"
	cran = "headliner" 

	version("0.0.3", md5="7362b98a277979903047aa458ac9ad8e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
