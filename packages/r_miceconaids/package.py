# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiceconaids(RPackage):
	"""Demand Analysis with the Almost Ideal Demand System (AIDS)

	Functions and tools
   for analysing consumer demand
   with the Almost Ideal Demand System (AIDS)
   suggested by Deaton and Muellbauer (1980).
	"""
	
	homepage = "http://www.micEcon.org"
	cran = "micEconAids" 

	version("0.6-20", md5="30eb44b3fa4ecd4f54f63181fe399fee")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-micecon@0.6.0:", type=("build", "run"))
	depends_on("r-systemfit@1.1.12:", type=("build", "run"))
	depends_on("r-misctools@0.6.0:", type=("build", "run"))
