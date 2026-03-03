# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArctools(RPackage):
	"""Processing and Physical Activity Summaries of Minute Level
Activity Data

	Provides functions to process minute level actigraphy-measured activity counts data and extract commonly used physical activity volume and fragmentation metrics.
	"""
	
	cran = "arctools" 

	version("1.1.6", md5="254e5ca571ccbd2bb3f520d0c378d558")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-runstats", type=("build", "run"))
