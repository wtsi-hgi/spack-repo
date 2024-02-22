# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesvl(RPackage):
	"""Visually Learning the Graphical Structure of Bayesian Networks
and Performing MCMC with 'Stan'

	Provides users with its associated functions for pedagogical purposes in visually learning Bayesian networks and Markov chain Monte Carlo (MCMC) computations. It enables users to: a) Create and examine the (starting) graphical structure of Bayesian networks; b) Create random Bayesian networks using a dataset with customized constraints; c) Generate 'Stan' code for structures of Bayesian networks for sampling the data and learning parameters; d) Plot the network graphs; e) Perform Markov chain Monte Carlo computations and produce graphs for posteriors checks. The package refers to one reference item, which describes the methods and algorithms: Vuong, Quan-Hoang and La, Viet-Phuong (2019) <doi:10.31219/osf.io/w5dx6> The 'bayesvl' R package. Open Science Framework (May 18).
	"""
	
	homepage = "https://github.com/sshpa/bayesvl"
	cran = "bayesvl" 

	version("0.8.5", md5="e3ebd478547c0153206516b4488612ca")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rstan@2.10:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
