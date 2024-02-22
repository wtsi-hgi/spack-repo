# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbalover(RPackage):
	"""Help Basketball Data Analysis

	Provides interface to the online basketball data resources such as
      Basketball reference API <https://www.basketball-reference.com/> and helps
      R users analyze basketball data.
	"""
	
	cran = "NBAloveR" 

	version("0.1.3.3", md5="79cae4552465d34673f94e2816470729")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
