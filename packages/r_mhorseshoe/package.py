# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhorseshoe(RPackage):
	"""Approximate Algorithm for Horseshoe Prior

	Provides an approximate algorithm for the horseshoe estimator
    used in Bayesian linear models. By implementing a sampler with high
    computational cost in the 'Rcpp' package and using an approximate algorithm
    that reduces matrix calculation complexity, parameter estimation speed for
    high-dimensional sparse data is faster. The approximate algorithm is
    described in Johndrow et al. (2020)
    <https://www.jmlr.org/papers/v21/19-536.html>.
	"""
	
	cran = "Mhorseshoe" 

	version("0.1.2", md5="c8a980ebac2fbe8d01d948f5c311b465")

	depends_on("r-rcpp", type=("build", "run"))
