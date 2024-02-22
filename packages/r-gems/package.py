# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGems(RPackage):
	"""Generalized Multistate Simulation Model

	Simulate and analyze multistate models with general hazard
    functions. gems provides functionality for the preparation of hazard functions
    and parameters, simulation from a general multistate model and predicting future
    events. The multistate model is not required to be a Markov model and may take
    the history of previous events into account. In the basic version, it allows
    to simulate from transition-specific hazard function, whose parameters are
    multivariable normally distributed.
	"""
	
	cran = "gems" 

	version("1.1.1", md5="631ca8a740a78f6addcb4b385c280443")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
