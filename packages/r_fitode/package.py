# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitode(RPackage):
	"""Tools for Ordinary Differential Equations Model Fitting

	Methods and functions for fitting ordinary differential equations (ODE) model in 'R'. Sensitivity equations are used to compute the gradients of ODE trajectories with respect to underlying parameters, which in turn allows for more stable fitting. Other fitting methods, such as MCMC (Markov chain Monte Carlo), are also available.
	"""
	
	cran = "fitode" 

	version("0.1.1", md5="d93417f9c4a728a53a91f494f6a1268c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
