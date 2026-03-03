# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoiwsa(RPackage):
	"""Seasonal Adjustment of Weekly Data

	Perform seasonal adjustment of weekly data. The package offers a user-friendly interface for computing seasonally adjusted estimates of weekly data and also includes diagnostic tools to assess the quality of the adjustments. Furthermore, it incorporates tools uniquely tailored to the specific characteristics of Israeli data. The method is described in more detail in Ginker (2023) <DOI:10.13140/RG.2.2.12221.44000>.
	"""
	
	homepage = "https://github.com/timginker/boiwsa"
	cran = "boiwsa" 

	version("1.0.0", md5="ec687d3209c1402a9ad758f09274c674")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
