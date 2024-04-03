# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVirtualpop(RPackage):
	"""Simulation of Populations by Sampling Waiting-Time Distributions

	Constructs a virtual population from fertility and mortality rates for any country,
	calendar year and birth cohort in the Human Mortality Database <https://www.mortality.org> and the Human Fertility Database <https://www.humanfertility.org>.  Fertility histories are simulated for every individual and their offspring, producing a multi-generation virtual population. 
	"""
	
	cran = "VirtualPop" 

	version("2.0.2", md5="353a0148f29a4d6e0ee8f554ed05542d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-hmdhfdplus", type=("build", "run"))
