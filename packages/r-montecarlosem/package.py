# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMontecarlosem(RPackage):
	"""Monte Carlo Data Simulation Package

	Monte Carlo simulation allows testing different conditions given to the correct structural equation models. This package runs Monte Carlo simulations under different conditions (such as sample size or normality of data). Within the package data sets can be simulated and run based on the given model.
  First, continuous and normal data sets are generated based on the given model. Later Fleishman's power method (1978) <DOI:10.1007/BF02293811> is used to add non-normality if exists. 
  When data generation is completed (or when generated data sets are given) model test can also be run.
  Please cite as "Orçan, F. (2021). MonteCarloSEM: An R Package to Simulate Data for SEM. International Journal of Assessment Tools in Education, 8 (3), 704-713."
	"""
	
	cran = "MonteCarloSEM" 

	version("0.0.7", md5="64f6da74104b52d3d482016bab7a78a7")
	version("0.0.6", md5="5a3870aaef835fd9230bc6eb3a6a8504")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
