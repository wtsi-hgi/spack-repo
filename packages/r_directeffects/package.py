# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirecteffects(RPackage):
	"""Estimating Controlled Direct Effects for Explaining Causal
Findings

	A set of functions to estimate the controlled direct effect of treatment fixing a potential mediator to a specific value. Implements the sequential g-estimation estimator described in Vansteelandt (2009) <doi:10.1097/EDE.0b013e3181b6f4c9> and Acharya, Blackwell, and Sen (2016) <doi:10.1017/S0003055416000216>.
	"""
	
	homepage = "https://www.mattblackwell.org/software/direct-effects/"
	cran = "DirectEffects" 

	version("0.2.1", md5="57535dbf27699c9b0ada7cff6d44b0fa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
