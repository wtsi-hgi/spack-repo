# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmtar(RPackage):
	"""Bayesian Approach for MTAR Models with Missing Data

	Implements parameter estimation using a Bayesian approach for Multivariate Threshold Autoregressive (MTAR) models with missing data using Markov Chain Monte Carlo methods. Performs the simulation of MTAR processes (mtarsim()), estimation of matrix parameters and the threshold values (mtarns()),  identification of the autoregressive orders using Bayesian variable selection (mtarstr()), identification of the number of regimes using Metropolised Carlin and Chib (mtarnumreg()) and estimate missing data, coefficients and covariance matrices conditional on the autoregressive orders, the threshold values and the number of regimes (mtarmissing()). Calderon and Nieto (2017) <doi:10.1080/03610926.2014.990758>.
	"""
	
	cran = "BMTAR" 

	version("0.1.1", md5="0298f0011087aa9b40e4dd43fb9363e6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-brobdingnag", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
