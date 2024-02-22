# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMplusparallelAutomation(RPackage):
	"""Parallel Processing Automation for 'Mplus'

	Offers automation tools to parallelize 'Mplus' operations when using 'R' for data generation. It facilitates streamlined integration between 'Mplus' and 'R', allowing users to run and manage multiple 'Mplus' models simultaneously and efficiently in 'R'.
	"""
	
	cran = "mplusParallel.automation" 

	version("0.0.1.1", md5="8bdff0d03b07462f7ded23ebe2fda46d")

	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
