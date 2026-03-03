# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayestreeprior(RPackage):
	"""Bayesian Tree Prior Simulation

	Provides a way to simulate from the prior distribution of Bayesian trees by Chipman et al. (1998) <DOI:10.2307/2669832>. The prior distribution of Bayesian trees is highly dependent on the design matrix X, therefore using the suggested hyperparameters by Chipman et al. (1998) <DOI:10.2307/2669832> is not recommended and could lead to unexpected prior distribution. This work is part of my master thesis (expected 2016).
	"""
	
	cran = "BayesTreePrior" 

	version("1.0.1", md5="a620f8056593167588bb45d89f97fc2d")

