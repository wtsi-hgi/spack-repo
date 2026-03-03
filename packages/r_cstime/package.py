# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCstime(RPackage):
	"""Date and Time Functions for Public Health Purposes

	Provides easy and consistent time conversion for public health purposes. The time conversion functions provided here are between date, ISO week, ISO yearweek, ISO year, calendar month/year, season, season week.  
	"""
	
	homepage = "https://www.csids.no/cstime/"
	cran = "cstime" 

	version("2023.5.3", md5="df7f7c64e0da8cbcb5178aee0df02b03")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
