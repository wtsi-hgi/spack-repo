# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsam(RPackage):
	"""Bayesian State-Space Models for Animal Movement

	Tools to fit Bayesian state-space models to animal tracking data. Models are provided for location 
    filtering, location filtering and behavioural state estimation, and their hierarchical versions. 
    The models are primarily intended for fitting to ARGOS satellite tracking data but options exist to fit 
    to other tracking data types. For Global Positioning System data, consider the 'moveHMM' package. 
    Simplified Markov Chain Monte Carlo convergence diagnostic plotting is provided but users are encouraged 
    to explore tools available in packages such as 'coda' and 'boa'.
	"""
	
	homepage = "<https://github.com/ianjonsen/bsam>"
	cran = "bsam" 

	version("1.1.3", md5="8b16e377a0268e85f4dd9b85ae6b3bfb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rjags@4.10:", type=("build", "run"))
	depends_on("r-coda@0.19.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-msm@1.6.8:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.1:", type=("build", "run"))
	depends_on("r-rworldxtra@1.1:", type=("build", "run"))
	depends_on("r-sp@1.2.3:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
