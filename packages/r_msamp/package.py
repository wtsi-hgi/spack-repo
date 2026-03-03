# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsamp(RPackage):
	"""Estimate Sample Size to Detect Bacterial Contamination in a
Product Lot

	Estimates the sample size needed to detect microbial contamination 
 in a lot with a user-specified detection probability and user-specified analytical sensitivity.
 Various patterns of microbial contamination are accounted for: homogeneous (Poisson), 
 heterogeneous (Poisson-Gamma) or localized(Zero-inflated Poisson).
  Ida Jongenburger et al. (2010) <doi:10.1016/j.foodcont.2012.02.004> 
  "Impact of microbial distributions on food safety".
  Leroy Simon (1963) <doi:10.1017/S0515036100001975>
  "Casualty Actuarial Society - The Negative Binomial and Poisson Distributions Compared". 
	"""
	
	cran = "msamp" 

	version("1.0.0", md5="67e357f2592d6807c96b3b86b6aad842")

