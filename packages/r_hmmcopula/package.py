# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmcopula(RPackage):
	"""Markov Regime Switching Copula Models Estimation and Goodness of
Fit

	R functions to estimate and perform goodness of fit test for several
    Markov regime switching and mixture bivariate copula models. 
    The goodness of fit test is based on a Cramer von Mises statistic and 
    uses the Rosenblatt transform and parametric bootstrap to estimate the p-value. 
    The estimation of the copula parameters are based on the pseudo-maximum likelihood
    method using pseudo-observations defined as normalized ranks.
	"""
	
	cran = "HMMcopula" 

	version("1.0.4", md5="641b58ee086b764654ef8d29d3b83598")

	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
