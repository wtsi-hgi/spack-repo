# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesfbhborrow(RPackage):
	"""Bayesian Dynamic Borrowing with Flexible Baseline Hazard
Function

	Allows Bayesian borrowing from a historical dataset for time-to-
    event data. A flexible baseline hazard function is achieved via a piecewise
    exponential likelihood with time varying split points and smoothing prior on the
    historic baseline hazards. The method is described in Scott and Lewin (2024) 
    <arXiv:2401.06082>.
	"""
	
	cran = "BayesFBHborrow" 

	version("1.0.1", md5="31abdc8596cce66c6ed2f8a99e9d0d7b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
