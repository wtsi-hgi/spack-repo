# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmcmc(RPackage):
	"""Tools for Analyzing MCMC Simulations from Bayesian Inference

	Tools for assessing and diagnosing convergence of
    Markov Chain Monte Carlo simulations, as well as for graphically display
    results from full MCMC analysis. The package also facilitates the graphical
    interpretation of models by providing flexible functions to plot the
    results against observed variables, and functions to work with
    hierarchical/multilevel batches of parameters
    (Fernández-i-Marín, 2016 <doi:10.18637/jss.v070.i09>).
	"""
	
	homepage = "http://xavier-fim.net/packages/ggmcmc/"
	cran = "ggmcmc" 

	version("1.5.1.1", md5="587ca05faf325d21a2367841c31f71cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally@1.1:", type=("build", "run"))
