# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesrecon(RPackage):
	"""Probabilistic Reconciliation via Conditioning

	Provides methods for probabilistic reconciliation of hierarchical forecasts of time series. The available methods include analytical Gaussian reconciliation (Corani et al., 2021) <doi:10.1007/978-3-030-67664-3_13>, MCMC reconciliation of count time series (Corani et al., 2022) <doi:10.48550/arXiv.2207.09322>, Bottom-Up Importance Sampling (Zambon et al., 2022) <doi:10.48550/arXiv.2210.02286>.
	"""
	
	cran = "bayesRecon" 

	version("0.2.0", md5="1d1b9b0196838a17f6d2a00fbec3831d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lpsolve@5.6.18:", type=("build", "run"))
