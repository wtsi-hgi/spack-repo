# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcpm(RPackage):
	"""Ordinal Outcomes: Generalized Linear Models with the Log Link

	An implementation of the Log Cumulative Probability Model (LCPM) 
  and Proportional Probability Model (PPM) for which the Maximum Likelihood Estimates are determined using constrained optimization. 
  This implementation accounts for the implicit constraints on the parameter space. Other 
  features such as standard errors, z tests and p-values use standard methods adapted from the results based on constrained optimization.
	"""
	
	cran = "lcpm" 

	version("0.1.1", md5="74bcec6e4cf7385655edb2a0ea27dbe9")

	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.11:", type=("build", "run"))
