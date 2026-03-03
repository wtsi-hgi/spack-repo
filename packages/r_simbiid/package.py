# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimbiid(RPackage):
	"""Simulation-Based Inference Methods for Infectious Disease Models

	Provides some code to run simulations of state-space models, and then
             use these in the Approximate Bayesian Computation Sequential Monte Carlo (ABC-SMC) 
             algorithm of Toni et al. (2009) <doi:10.1098/rsif.2008.0172> and a bootstrap particle
             filter based particle Markov chain Monte Carlo (PMCMC) algorithm 
             (Andrieu et al., 2010 <doi:10.1111/j.1467-9868.2009.00736.x>). 
             Also provides functions to plot and summarise the outputs.
	"""
	
	homepage = "https://github.com/tjmckinley/SimBIID"
	cran = "SimBIID" 

	version("0.2.1", md5="2791661c2aea5ccc98ecde8f9c2e3944")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppxptrutils", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
