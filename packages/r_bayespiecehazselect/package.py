# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayespiecehazselect(RPackage):
	"""Variable Selection in a Hierarchical Bayesian Model for a Hazard
Function

	Fits a piecewise exponential hazard to survival data using a
    Hierarchical Bayesian model with an Intrinsic Conditional Autoregressive
    formulation for the spatial dependency in the hazard rates for each piece.
    This function uses Metropolis- Hastings-Green MCMC to allow the number of split
    points to vary and also uses Stochastic Search Variable Selection to determine
    what covariates drive the risk of the event. This function outputs trace plots
    depicting the number of split points in the hazard and the number of variables
    included in the hazard. The function saves all posterior quantities to the
    desired path.
	"""
	
	cran = "BayesPieceHazSelect" 

	version("1.1.0", md5="596b886312e1771728ead04192bff74d")

	depends_on("r-mvtnorm", type=("build", "run"))
