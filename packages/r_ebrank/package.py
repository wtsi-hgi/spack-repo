# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbrank(RPackage):
	"""Empirical Bayes Ranking

	Empirical Bayes ranking applicable to parallel-estimation settings where the estimated parameters are asymptotically unbiased and normal, with known standard errors.  A mixture normal prior for each parameter is estimated using Empirical Bayes methods, subsequentially ranks for each parameter are simulated from the resulting joint posterior over all parameters (The marginal posterior densities for each parameter are assumed independent). Finally, experiments are ordered by expected posterior rank, although computations minimizing other plausible rank-loss functions are also given.  
	"""
	
	cran = "EBrank" 

	version("1.0.0", md5="d79d66a473d40a0214b26f4d0074edf3")

	depends_on("r@3.2.4:", type=("build", "run"))
