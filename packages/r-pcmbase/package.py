# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcmbase(RPackage):
	"""Simulation and Likelihood Calculation of Phylogenetic
Comparative Models

	Phylogenetic comparative methods represent models of continuous trait 
  data associated with the tips of a phylogenetic tree. Examples of such models 
  are Gaussian continuous time branching stochastic processes such as Brownian 
  motion (BM) and Ornstein-Uhlenbeck (OU) processes, which regard the data at the 
  tips of the tree as an observed (final) state of a Markov process starting from 
  an initial state at the root and evolving along the branches of the tree. The 
  PCMBase R package provides a general framework for manipulating such models. 
  This framework consists of an application programming interface for specifying 
  data and model parameters, and efficient algorithms for simulating trait evolution 
  under a model and calculating the likelihood of model parameters for an assumed
  model and trait data. The package implements a growing collection of models, 
  which currently includes BM, OU, BM/OU with jumps, two-speed OU as well as mixed 
  Gaussian models, in which different types of the above models can be associated 
  with different branches of the tree. The PCMBase package is limited to 
  trait-simulation and likelihood calculation of (mixed) Gaussian phylogenetic 
  models. The PCMFit package provides functionality for inference of 
  these models to tree and trait data. The package web-site 
  <https://venelin.github.io/PCMBase/>
  provides access to the documentation and other resources. 
	"""
	
	homepage = "https://venelin.github.io/PCMBase/"
	cran = "PCMBase" 

	version("1.2.14", md5="9be7d13a1bb7e3c099e2273282d7c194")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
