# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPttstability(RPackage):
	"""Particle-Takens Stability

	Includes a collection of functions presented in "Measuring stability in ecological systems without static equilibria" by Clark et al. (2022) <doi:10.1002/ecs2.4328> in Ecosphere.
	These can be used to estimate the parameters of a stochastic state space model (i.e. a model where
	a time series is observed with error). The goal of this package is to estimate the variability
	around a deterministic process, both in terms of observation error - i.e. variability due to
	imperfect observations that does not influence system state - and in terms of process noise - i.e.
	stochastic variation in the actual state of the process. Unlike classical methods for estimating
	variability, this package does not necessarily assume that the deterministic state is fixed (i.e.
	a fixed-point equilibrium), meaning that variability around a dynamic trajectory can be estimated
	(e.g. stochastic fluctuations during predator-prey dynamics).
	"""
	
	cran = "pttstability" 

	version("1.4", md5="18ced71962d0bcfe1fd999f7dc58819f")

	depends_on("r@3.4:", type=("build", "run"))
