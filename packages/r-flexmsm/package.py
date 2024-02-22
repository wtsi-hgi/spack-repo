# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexmsm(RPackage):
	"""A General Framework for Flexible Multi-State Survival Modelling

	A general estimation framework for multi-state Markov processes with flexible specification of the transition intensities.
    The log-transition intensities can be specified through Generalised Additive Models which allow for virtually any type of covariate
    effect. Elementary specifications such as time-homogeneous processes and simple parametric forms are also supported. There are 
    no limitations on the type of process one can assume, with both forward and backward transitions allowed and virtually any number
    of states.
	"""
	
	cran = "flexmsm" 

	version("0.1.1", md5="295ab1247fc55529f283f153e5fb515e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gjrm", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
