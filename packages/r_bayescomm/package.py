# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayescomm(RPackage):
	"""Bayesian Community Ecology Analysis

	Bayesian multivariate binary (probit) regression
    models for analysis of ecological communities.
	"""
	
	cran = "BayesComm" 

	version("0.1-2", md5="d221f97ce75e0f6c37d692d60e9e26b8")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
