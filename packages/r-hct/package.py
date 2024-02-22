# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHct(RPackage):
	"""Calculates Significance Criteria and Power for a Single Arm
Trial

	Given a database of previous treatment/placebo estimates, their standard errors and sample sizes,
      the program calculates a significance criteria and power estimate that takes into account the among
      trial variation.
	"""
	
	cran = "HCT" 

	version("0.1.3", md5="0a5f2020870f62e3139c95ea8855df7e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
