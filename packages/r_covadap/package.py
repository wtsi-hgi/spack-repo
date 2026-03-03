# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovadap(RPackage):
	"""Implement Covariate-Adaptive Randomization

	Implementing seven Covariate-Adaptive Randomization to assign patients to two treatments. 
    Three of these procedures can also accommodate quantitative and mixed covariates. Given a set of covariates, the user can
    generate a single sequence of allocations or replicate the design multiple times by simulating the patients' covariate
    profiles. At the end, an extensive assessment of the performance of the randomization procedures is provided, calculating
    several imbalance measures. See Baldi Antognini A, Frieri R, Zagoraiou M and Novelli M (2022) <doi:10.1007/s00362-022-01381-1> for details.
	"""
	
	cran = "covadap" 

	version("1.0.1", md5="5aabfe39832f0e10c6d77d6293edd392")

