# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebinfer(RPackage):
	"""Bayesian Inference for Differential Equations

	A Bayesian framework for parameter inference in differential equations.
    This approach offers a rigorous methodology for parameter inference as well as
    modeling the link between unobservable model states and parameters, and
    observable quantities. Provides templates for the DE model, the
    observation model and data likelihood, and the model parameters and their prior
    distributions. A Markov chain Monte Carlo (MCMC) procedure processes these inputs
    to estimate the posterior distributions of the parameters and any derived
    quantities, including the model trajectories. Further functionality is provided
    to facilitate MCMC diagnostics and the visualisation of the posterior distributions
    of model parameters and trajectories.
	"""
	
	homepage = "https://github.com/pboesu/debinfer"
	cran = "deBInfer" 

	version("0.4.4", md5="a567122a20ed900395206121ba1be80e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pbsddesolve", type=("build", "run"))
