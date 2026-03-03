# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistributacalcul(RPackage):
	"""Probability Distribution Functions

	Calculates expected values, variance, different moments (kth 
    moment, truncated mean), stop-loss, mean excess loss, Value-at-Risk (VaR)
    and Tail Value-at-Risk (TVaR) as well as some density and cumulative 
    (survival) functions of continuous, discrete and compound distributions. 
    This package also includes a visual 'Shiny' component to enable students 
    to visualize distributions and understand the impact of their parameters.
    This package is intended to expand the 'stats' package so as
    to enable students to develop an intuition for probability.
	"""
	
	homepage = "https://alec42.github.io/Distributacalcul_Package/"
	cran = "Distributacalcul" 

	version("0.4.0", md5="974e074bdefb0b4f54110874e2c88fb5")

	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
