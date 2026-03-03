# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcstats(RPackage):
	"""Visualize Results of Statistical Hypothesis Tests

	Provides functionality to produce graphs of sampling distributions of test 	statistics from a variety of common statistical tests. With only a few keystrokes, 	the user can conduct a hypothesis test and visualize the test statistic and 		corresponding p-value through the shading of its sampling distribution. Initially       	created for statistics at Middlebury College.
	"""
	
	cran = "mcStats" 

	version("0.1.2", md5="f915ae1b315a6fbc2559a2044f5f57fd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
