# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmrm(RPackage):
	"""Bayesian Multivariate Receptor Modeling

	Bayesian analysis of multivariate receptor modeling. The package consists of implementations of the methods of Park and Oh (2015) <doi:10.1016/j.chemolab.2015.08.021>.The package uses 'JAGS'(Just Another Gibbs Sampler) to generate Markov chain Monte Carlo samples of parameters. 
	"""
	
	cran = "bayesMRM" 

	version("2.4.0", md5="9ec991ae35cf2c010eee4df087676671")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
