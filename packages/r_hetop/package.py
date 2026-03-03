# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHetop(RPackage):
	"""MLE and Bayesian Estimation of Heteroskedastic Ordered Probit
(HETOP) Model

	Provides functions for maximum likelihood and Bayesian estimation of the Heteroskedastic Ordered Probit (HETOP) model, using methods described in Lockwood, Castellano and Shear (2018) <doi:10.3102/1076998618795124> and Reardon, Shear, Castellano and Ho (2017) <doi:10.3102/1076998616666279>.  It also provides a general function to compute the triple-goal estimators of Shen and Louis (1998) <doi:10.1111/1467-9868.00135>.
	"""
	
	cran = "HETOP" 

	version("0.2-6", md5="9fe5254dd34d06e228a7895f2a47134d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
