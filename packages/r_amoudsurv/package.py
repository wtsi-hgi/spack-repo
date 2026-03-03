# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmoudsurv(RPackage):
	"""Tractable Parametric Odds-Based Regression Models

	Fits tractable fully parametric odds-based regression models for survival data, including proportional odds (PO), accelerated failure time (AFT), accelerated odds (AO), and General Odds (GO) models in overall survival frameworks. Given at least an R function specifying the survivor, hazard rate and cumulative distribution functions, any user-defined parametric distribution can be fitted. We applied and evaluated a minimum of seventeen (17) various baseline distributions that can handle different failure rate shapes for each of the four different proposed odds-based regression models. For more information see Bennet et al., (1983) <doi:10.1002/sim.4780020223>, and Muse et al., (2022) <doi:10.1016/j.aej.2022.01.033>.
	"""
	
	cran = "AmoudSurv" 

	version("0.1.0", md5="90448f07280396709a12e0d9b4b2b322")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ahsurv", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
