# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustaft(RPackage):
	"""Truncated Maximum Likelihood Fit and Robust Accelerated Failure
Time Regression for Gaussian and Log-Weibull Case

	R functions for the computation of the truncated maximum
	     likelihood and the robust accelerated failure time regression 
	     for gaussian and log-Weibull case.
	"""
	
	cran = "RobustAFT" 

	version("1.4-7", md5="16c1db2b592611625782b4a0797e3b2a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-deoptimr", type=("build", "run"))
