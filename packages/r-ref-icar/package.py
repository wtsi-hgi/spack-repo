# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefIcar(RPackage):
	"""Objective Bayes Intrinsic Conditional Autoregressive Model for
Areal Data

	Implements an objective Bayes intrinsic conditional autoregressive 
    prior. This model provides an objective Bayesian approach for modeling spatially 
    correlated areal data using an intrinsic conditional autoregressive prior on a vector of 
    spatial random effects.
	"""
	
	cran = "ref.ICAR" 

	version("2.0.1", md5="688489fd6145cb3c0162bae07a97d467")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
