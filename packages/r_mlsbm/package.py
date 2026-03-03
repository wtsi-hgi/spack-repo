# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlsbm(RPackage):
	"""Efficient Estimation of Bayesian SBMs & MLSBMs

	Fit Bayesian stochastic block models (SBMs) and multi-level stochastic block models (MLSBMs) using efficient Gibbs sampling implemented in 'Rcpp'. The models assume symmetric, non-reflexive graphs (no self-loops) with unweighted, binary edges. Data are input as a symmetric binary adjacency matrix (SBMs), or list of such matrices (MLSBMs). 
	"""
	
	cran = "mlsbm" 

	version("0.99.2", md5="077461d228b32f402ded30312a45b391")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
