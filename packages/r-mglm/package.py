# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMglm(RPackage):
	"""Multivariate Response Generalized Linear Models

	Provides functions that (1) fit multivariate discrete distributions, (2) generate random numbers from multivariate discrete distributions, and (3) run regression and penalized regression on the multivariate categorical response data.  Implemented models include: multinomial logit model, Dirichlet multinomial model, generalized Dirichlet multinomial model, and negative multinomial model. Making the best of the minorization-maximization (MM) algorithm and Newton-Raphson method, we derive and implement stable and efficient algorithms to find the maximum likelihood estimates. On a multi-core machine, multi-threading is supported.
	"""
	
	cran = "MGLM" 

	version("0.2.1", md5="d4c964eaa6fd83920fd9948ade55a0f4")

	depends_on("r@3:", type=("build", "run"))
