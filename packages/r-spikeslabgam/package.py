# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikeslabgam(RPackage):
	"""Bayesian Variable Selection and Model Choice for Generalized
Additive Mixed Models

	Bayesian variable selection, model choice, and regularized
    estimation for (spatial) generalized additive mixed regression models
    via stochastic search variable selection with spike-and-slab priors.
	"""
	
	homepage = "https://github.com/fabian-s/spikeSlabGAM"
	cran = "spikeSlabGAM" 

	version("1.1-19", md5="b811b90c18c8934bad45d48fb3ec0740")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-r2winbugs", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
