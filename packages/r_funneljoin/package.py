# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunneljoin(RPackage):
	"""Time-Based Joins to Analyze Sequences of Events

	Time-based joins to analyze sequence of events, 
    both in memory and out of memory. after_join() joins two 
    tables of events, while funnel_start() and funnel_step() 
    join events in the same table. With the type argument, you
    can switch between different funnel types, like first-first
    and last-firstafter.
	"""
	
	cran = "funneljoin" 

	version("0.2.0", md5="d50d31171e32132db928c7447619857f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
