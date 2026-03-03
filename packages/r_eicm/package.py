# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REicm(RPackage):
	"""Explicit Interaction Community Models

	Model fitting and species biotic interaction network topology selection for explicit
  interaction community models. Explicit interaction community models are an extension of binomial
  linear models for joint modelling of species communities, that incorporate both the effects of
  species biotic interactions and the effects of missing covariates. Species interactions are modelled
  as direct effects of each species on each of the others, and are estimated alongside the effects of
  missing covariates, modelled as latent factors. The package includes a penalized maximum likelihood
  fitting function, and a genetic algorithm for selecting the most parsimonious species interaction
  network topology.
	"""
	
	homepage = "https://github.com/miguel-porto/eicm"
	cran = "eicm" 

	version("1.0.3", md5="29ddd6a785bb1ac8317b3d40263809d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ga@3.1.1:", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
