# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbrf(RPackage):
	"""Time-Based Rolling Functions

	Provides rolling statistical functions based
    on date and time windows instead of n-lagged observations.
	"""
	
	homepage = "https://mps9506.github.io/tbrf/"
	cran = "tbrf" 

	version("0.1.5", md5="ef7ddfc7f751f1c44854e2c3f0b81f19")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
