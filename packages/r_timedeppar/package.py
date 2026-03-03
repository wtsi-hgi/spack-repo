# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimedeppar(RPackage):
	"""Infer Constant and Stochastic, Time-Dependent Model Parameters

	Infer constant and stochastic, time-dependent parameters to consider intrinsic stochasticity of a dynamic model and/or to analyze model structure modifications that could reduce model deficits.
  The concept is based on inferring time-dependent parameters as stochastic processes in the form of Ornstein-Uhlenbeck processes jointly with inferring constant model parameters and parameters of the Ornstein-Uhlenbeck processes.
  The package also contains functions to sample from and calculate densities of Ornstein-Uhlenbeck processes.
  References:
  Tomassini, L., Reichert, P., Kuensch, H.-R. Buser, C., Knutti, R. and Borsuk, M.E. (2009), A smoothing algorithm for estimating stochastic, continuous-time model parameters and its application to a simple climate model, Journal of the Royal Statistical Society: Series C (Applied Statistics) 58, 679-704, <doi:10.1111/j.1467-9876.2009.00678.x>
  Reichert, P., and Mieleitner, J. (2009), Analyzing input and structural uncertainty of nonlinear dynamic models with stochastic, time-dependent parameters. Water Resources Research, 45, W10402, <doi:10.1029/2009WR007814>
  Reichert, P., Ammann, L. and Fenicia, F. (2021), Potential and challenges of investigating intrinsic uncertainty of hydrological models with time-dependent, stochastic parameters. Water Resources Research 57(8), e2020WR028311, <doi:10.1029/2020WR028311>
  Reichert, P. (2022), timedeppar: An R package for inferring stochastic, time-dependent model parameters, in preparation.
	"""
	
	homepage = "https://gitlab.com/p.reichert/timedeppar"
	cran = "timedeppar" 

	version("1.0.3", md5="0738f78fa2d1a95b0bd8af0dfdb1ba63")

	depends_on("r-mvtnorm", type=("build", "run"))
