# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcecens(RPackage):
	"""Ordered Composite Endpoints with Censoring

	Estimates win ratio or Mann-Whitney parameter for two group
 comparisons using ordered composite endpoints with right censoring
 as described in Follmann, Fay, Hamasaki, and Evans (2020)<doi:10.1002/sim.7890>.
	"""
	
	cran = "oceCens" 

	version("0.1.2", md5="4b712168c88f3170a69669194472620b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
