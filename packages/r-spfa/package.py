# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpfa(RPackage):
	"""Semi-Parametric Factor Analysis

	Estimation, scoring, and plotting functions for the semi-parametric factor model proposed by Liu & Wang (2022) <doi:10.1007/s11336-021-09832-8> and Liu & Wang (2023) <arXiv:2303.10079>. Both the conditional densities of observed responses given the latent factors and the joint density of latent factors are estimated non-parametrically. Functional parameters are approximated by smoothing splines, whose coefficients are estimated by penalized maximum likelihood using an expectation-maximization (EM) algorithm. E- and M-steps can be parallelized on multi-thread computing platforms that support 'OpenMP'. Both continuous and unordered categorical response variables are supported.
	"""
	
	cran = "spfa" 

	version("1.0", md5="831815cf578690ecae7bfc4e12ddffbf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
