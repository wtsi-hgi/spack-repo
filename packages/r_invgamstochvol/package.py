# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvgamstochvol(RPackage):
	"""Obtains the Log Likelihood for an Inverse Gamma Stochastic
Volatility Model

	Computes the log likelihood for an inverse gamma stochastic volatility model using a closed form expression of the likelihood. The details of the computation of this closed form expression are given in Gonzalez and Majoni (2023) <http://rcea.org/RePEc/pdf/wp23-11.pdf> .  
    The closed form expression is obtained for a stationary inverse gamma stochastic volatility model by marginalising out the volatility. This allows the user to obtain the maximum likelihood estimator for this non linear non Gaussian state space model. In addition, the user can obtain the estimates of the smoothed volatility using the exact smoothing distributions.
	"""
	
	cran = "invgamstochvol" 

	version("1.0.0", md5="b493856062d053eb79a6756641c11546")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
