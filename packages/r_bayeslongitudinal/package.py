# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayeslongitudinal(RPackage):
	"""Adjust Longitudinal Regression Models Using Bayesian Methodology

	Adjusts longitudinal regression models using Bayesian methodology 
            for covariance structures of composite symmetry (SC), 
            autoregressive ones of order 1 AR (1) and 
            autoregressive moving average of order (1,1) ARMA (1,1).
	"""
	
	cran = "bayeslongitudinal" 

	version("0.1.0", md5="5193caef6a1d6a3a81933be099c24c05")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-learnbayes", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
